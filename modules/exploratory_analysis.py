import streamlit as st
import pandas as pd
import plotly.express as px

def run_eda_module():
    st.header("2. Exploratory Data Analysis")
    
    if "df" not in st.session_state:
        st.warning("⚠️ Please upload a dataset first in the Dataset module.")
        return
    
    df = st.session_state["df"]
    
    tab1, tab2, tab3 = st.tabs(["Overview", "Service Analysis", "Visualizations"])
    
    with tab1:
        st.subheader("Data Overview")
        st.dataframe(df.describe(include="all"))
        st.write(f"**SLA Breach Count:** {df['SLA_Breached'].sum()} out of {len(df)}")
    
    with tab2:
        st.subheader("Breach Rate by Service Type")
        service_stats = df.groupby("Service_Type")["SLA_Breached"].agg(["count", "mean"])
        service_stats["mean"] = service_stats["mean"] * 100
        service_stats = service_stats.round(2)
        service_stats.columns = ["Total Requests", "Breach Rate (%)"]
        st.dataframe(service_stats)
    
    with tab3:
        st.subheader("Charts")
        fig1 = px.bar(df, x="Service_Type", color="SLA_Breached", 
                      title="SLA Breaches by Service Type",
                      barmode="group")
        st.plotly_chart(fig1, use_container_width=True)
        
        fig2 = px.pie(df, names="Queue_Category", title="Queue Category Distribution")
        st.plotly_chart(fig2, use_container_width=True)