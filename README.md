# 📊 Customer Churn Prediction Dashboard

An AI-powered web application that predicts whether a telecom customer is likely to churn (leave the service) using Machine Learning, along with an interactive Streamlit dashboard for real-time risk analysis.

## 🚀 Features
- Real-time churn prediction based on customer inputs
- Churn probability score with risk level (High/Low Risk)
- Interactive gauge chart visualization of churn risk
- Clean, dark-themed, responsive dashboard UI

## 🧠 How It Works
1. Customer data (tenure, charges, gender, partner, dependents, etc.) is collected via the dashboard
2. Categorical inputs are encoded to match the trained model's feature format
3. A **Random Forest Classifier** (tuned via GridSearchCV) predicts churn probability
4. The app displays the prediction, probability score, and risk level with a gauge chart

## 📊 Dataset
- Telco Customer Churn dataset (7,043 customers, 21 features)
- Churn distribution: 5,174 No / 1,869 Yes
- Features include tenure, monthly charges, total charges, contract type, internet service, payment method, and more

## 🛠️ Tech Stack
- **Language:** Python
- **Machine Learning:** Scikit-learn (Logistic Regression, Random Forest, GridSearchCV)
- **Web Framework:** Streamlit
- **Visualization:** Plotly (Gauge Chart)
- **Model Serialization:** Pickle

## 📈 Model Performance
- Logistic Regression Accuracy: 78.7%
- Random Forest Accuracy: 78.5%
- Best Random Forest (GridSearchCV tuned) Accuracy: 78.7%
- Top predictive features: Total Charges, Monthly Charges, Tenure

## 📂 Project Structure
├── app.py                     # Streamlit web application
├── churn_prediction.ipynb     # Model training & analysis notebook
├── models/
│   ├── churn_model.pkl        # Trained Random Forest model
│   └── model_columns.pkl      # Feature columns used for prediction
├── requirements.txt           # Project dependencies
└── README.md

## ⚙️ Installation & Usage
1. Clone the repository
git clone https://github.com/gagan6571/Churn-prediction.git
cd Churn-prediction

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run app.py

## 🖥️ Dashboard Features
- **Customer Information Input:** Tenure, monthly charges, total charges, gender, partner, dependents, phone service, paperless billing
- **Churn Probability:** Displays likelihood of customer churn as a percentage
- **Risk Level:** Classifies customer as High Risk or Low Risk
- **Gauge Chart:** Visual representation of churn risk score
- **Prediction Result:** Clear churn/no-churn outcome

## 📌 Note
This project is for educational purposes and demonstrates a complete churn prediction pipeline using classical Machine Learning techniques with hyperparameter tuning.
