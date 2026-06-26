from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from psycopg2.pool import SimpleConnectionPool
import psycopg2
import pickle
import numpy as np

app = FastAPI()

# -----------------------------
# PostgreSQL Connection Pool
# -----------------------------
pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host="localhost",
    database="fraud",
    user="postgres",
    password="123934",   # Use string
)

# -----------------------------
# Load Pickle Files
# -----------------------------
with open("Mall_Customers_0.pkl", "rb") as f:
    model = pickle.load(f)

with open("Mall_Customers_1.pkl", "rb") as f:
    scaler = pickle.load(f)

# -----------------------------
# Pydantic Schema
# -----------------------------
class Customer(BaseModel):
    age: int
    annual_income: float
    spending_score: float

# -----------------------------
# Home API
# -----------------------------
@app.get("/")
def home():
    return {"message": "Customer Segmentation API"}

# -----------------------------
# Prediction API
# -----------------------------
@app.post("/predict")
def predict(customer: Customer):

    # Prepare input data
    data = np.array([[
        customer.annual_income,
        customer.spending_score,
        customer.age
    ]])

    # Scale input
    data_scaled = scaler.transform(data)

    # Predict cluster
    cluster = int(model.predict(data_scaled)[0])

    conn = None
    cursor = None

    try:
        # Get a connection from the pool
        conn = pool.getconn()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customers
            (age, annual_income, spending_score, cluster)
            VALUES (%s, %s, %s, %s)
            """,
            (
                customer.age,
                customer.annual_income,
                customer.spending_score,
                cluster,
            ),
        )

        conn.commit()

        return {
            "Age": customer.age,
            "Annual Income": customer.annual_income,
            "Spending Score": customer.spending_score,
            "Predicted Cluster": cluster,
        }

    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            pool.putconn(conn)

# -----------------------------
# Close Pool on Shutdown
# -----------------------------
@app.on_event("shutdown")
def shutdown():
    pool.closeall()