import streamlit as st
import pandas as pd

def run_prediction_module(model):
    st.header("3. SLA Breach Prediction")
    
    st.subheader("Enter Request Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        service = st.selectbox("Service_Type", 
            ["Admission", "Enrollment", "Grading", "Records", "ID Issuance"])
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        queue_cat = st.selectbox("Queue_Category", ["Low", "Medium", "High"])
    
    with col2:
        office = st.selectbox("Assigned_Office", 
            ["Registrar", "Student Affairs", "Finance", "Academic", "IT Services"])
        weekday = st.slider("Submission_Weekday (0=Mon, 6=Sun)", 0, 6, 2)
    
    predict_btn = st.button("🔍 Predict SLA Breach Risk")
    
    if predict_btn:
        input_data = pd.DataFrame([{
            "Service_Type": service,
            "Priority": priority,
            "Queue_Category": queue_cat,
            "Assigned_Office": office,
            "Submission_Weekday": weekday
        }])
        
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0].max() * 100
        
        if prediction == 1:
            st.error(f"⚠️ **HIGH RISK** — Likely to breach SLA ({proba:.1f}% confidence)")
            st.info("Recommendation: Assign higher priority or additional staff.")
        else:
            st.success(f"✅ **LOW RISK** — Within expected processing time ({proba:.1f}% confidence)")
            st.info("Recommendation: Proceed with standard processing.")