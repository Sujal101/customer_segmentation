import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Segmentation")

st.write("Enter customer details to predict the cluster.")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

annual_income = st.number_input(
    "Annual Income (k$)",
    min_value=0.0,
    value=50.0
)

spending_score = st.number_input(
    "Spending Score",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

if st.button("Predict Cluster"):

    data = {
        "age": age,
        "annual_income": annual_income,
        "spending_score": spending_score
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    if response.status_code == 200:

        result = response.json()

        st.success("Prediction Successful")

        st.write("### Prediction Result")

        st.write(f"**Age:** {result['Age']}")
        st.write(f"**Annual Income:** {result['Annual Income']}")
        st.write(f"**Spending Score:** {result['Spending Score']}")
        st.write(f"### Predicted Cluster: {result['Predicted Cluster']}")

    else:
        st.error(response.text)