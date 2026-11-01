import streamlit as st
import pandas as pd
import joblib
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "modules")))

from data_processing import run_dataset_module
from exploratory_analysis import run_eda_module
from prediction import run_prediction_module
from dashboard import run_dashboard_module
from sad_integration import run_sad_module

st.set_page_config(
    page_title="SAD Predictive System — Student Service Monitoring",
    layout="wide"
)

menu = st.sidebar.selectbox(
    "Module",
    ["Home", "Dataset", "EDA", "Prediction", "Dashboard", "System Design"]
)

@st.cache_resource
def load_model():
    
    model_path = os.path.join(os.path.dirname(__file__), "trained_model.joblib")
    return joblib.load(model_path)

model = load_model()

if menu == "Home":
    st.title("📊 Student Service Request Monitoring System")
    st.subheader("Predict SLA (Service-Level Agreement) Breaches")
    st.info("""
    This system reuses the Decision Tree model trained in your Midterm Examination.
    Predictions are decision-support only — NOT automatic approval or denial.
    Authorized student services staff must review and record final decisions.
    """)
    st.markdown("""
    **Modules:**
    1. Dataset — Upload CSV, validate schema, preview data
    2. EDA — Statistics, distribution, 3+ interactive charts
    3. Prediction — Input request details → get breach risk + confidence
    4. Dashboard — KPIs, workload, recommendations
    5. System Design — SAD requirements, use case diagram, workflow
    """)

elif menu == "Dataset":
    run_dataset_module()
elif menu == "EDA":
    run_eda_module()
elif menu == "Prediction":
    run_prediction_module(model)
elif menu == "Dashboard":
    run_dashboard_module()
elif menu == "System Design":
    run_sad_module()
