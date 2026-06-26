# Customer Segmentation using K-Means Clustering

## Project Overview

This project performs **Customer Segmentation** using the **K-Means Clustering** algorithm. The trained model predicts which customer segment a new customer belongs to based on:

- Age
- Annual Income
- Spending Score

The project includes:

- Machine Learning using Scikit-learn
- FastAPI REST API
- Streamlit User Interface
- PostgreSQL Database Integration

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- FastAPI
- Streamlit
- PostgreSQL
- Pickle

---

## Project Structure

```
customer_segmentation/
│
├── Mall_Customers.csv
├── Mall_Customers_0.pkl
├── Mall_Customers_1.pkl
├── segmentation.py
├── fast_api.py
├── ui.py
├── README.md
└── requirements.txt
```

---

## Clone Repository

```bash
git clone https://github.com/Sujal101/customer_segmentation.git
```

Move into the project folder:

```bash
cd customer_segmentation
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi uvicorn streamlit pandas numpy scikit-learn matplotlib seaborn psycopg2-binary pydantic
```

---

## Train the Model

```bash
python segmentation.py
```

This creates:

- Mall_Customers_0.pkl
- Mall_Customers_1.pkl

---

## Run FastAPI

```bash
uvicorn fast_api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

Open another terminal.

```bash
streamlit run ui.py
```

---

## API Input

```json
{
  "age": 25,
  "annual_income": 70,
  "spending_score": 85
}
```

---

## API Response

```json
{
  "Age": 25,
  "Annual Income": 70,
  "Spending Score": 85,
  "Predicted Cluster": 2
}
```

---

## Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Scaling
4. Train K-Means Model
5. Save Model using Pickle
6. Load Model in FastAPI
7. Predict Customer Cluster
8. Store Prediction in PostgreSQL
9. Display Result in Streamlit

---

## Author

**Sujal101**

GitHub: https://github.com/Sujal101
