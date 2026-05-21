import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

# Page Config
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
    initial_sidebar_state="expanded"
)

# Load Model
model = pickle.load(open('churn_model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.stButton>button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title(" Customer Churn Prediction Dashboard")

st.markdown("### AI Powered Customer Retention System")

# Sidebar
st.sidebar.header("Customer Information")

# Layout
col1, col2 = st.columns(2)

with col1:

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        value=50.0
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

with col2:

    TotalCharges = st.number_input(
        "Total Charges",
        value=500.0
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

# Predict Button
if st.button("Predict Churn"):

    input_data = {
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,

        'gender_Male': 1 if gender == "Male" else 0,

        'Partner_Yes': 1 if Partner == "Yes" else 0,

        'Dependents_Yes': 1 if Dependents == "Yes" else 0,

        'PhoneService_Yes': 1 if PhoneService == "Yes" else 0,

        'PaperlessBilling_Yes': 1 if PaperlessBilling == "Yes" else 0
    }

    input_df = pd.DataFrame([input_data])

    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[model_columns]

    # Prediction
    prediction = model.predict(input_df)[0]

    # Probability
    probability = model.predict_proba(input_df)[0][1]

    st.markdown("---")

    # KPI Cards
    kpi1, kpi2 = st.columns(2)

    with kpi1:
        st.metric(
            label="Churn Probability",
            value=f"{probability*100:.2f}%"
        )

    with kpi2:
        risk = "High Risk" if probability > 0.5 else "Low Risk"

        st.metric(
            label="Risk Level",
            value=risk
        )

    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Churn Risk"},
        gauge={
            'axis': {'range': [0, 100]}
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    # Final Result
    if prediction == 1:
        st.error(" Customer Will Churn")
    else:
        st.success(" Customer Will Not Churn")
