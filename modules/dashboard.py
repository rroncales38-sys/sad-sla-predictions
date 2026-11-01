import streamlit as st
import pandas as pd

def run_dashboard_module():
    st.header("4. Performance Dashboard")
    
    if "df" not in st.session_state:
        st.warning("⚠️ Please upload a dataset first in the Dataset module.")
        return
    
    df = st.session_state["df"]
    
    col1, col2, col3, col4 = st.columns(4)
    
    total = len(df)
    breaches = df["SLA_Breached"].sum()
    breach_pct = (breaches / total * 100).round(1)
    avg_days = df["Processing_Days"].mean().round(1)
    
    col1.metric("Total Requests", total)
    col2.metric("SLA Breaches", breaches)
    col3.metric("Breach Rate", f"{breach_pct}%")
    col4.metric("Avg Processing Days", avg_days)
    
    st.subheader("Recommendations")
    st.info("""
    • High-volume services with breach rates above 30% should be prioritized for process review.
    • During High queue categories, consider reallocating staff from low-demand areas.
    • Monday–Wednesday submissions show higher volume → prepare extra support.
    """)