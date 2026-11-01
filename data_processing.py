import streamlit as st
import pandas as pd

EXPECTED_COLUMNS_RAW = [
    "Request_ID", "Service_Type", "Requester_Type", "Request_Channel",
    "Priority", "Assigned_Office", "Queue_Length", "Status",
    "Processing_Days", "SLA_Days", "satisfaction_Score", "Submission_Date"
]

def run_dataset_module():
    st.header("1. Dataset Upload & Validation")
    
    uploaded_file = st.file_uploader("Upload your CSV Dataset", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        st.subheader("Dataset Preview")
        st.dataframe(df.head(10))
        
        st.subheader("Dataset Info")
        st.write(f"**Total Rows:** {df.shape[0]}")
        st.write(f"**Total Columns:** {df.shape[1]}")

        df_processed = df.copy()
        
        df_processed["Submission_Date"] = pd.to_datetime(df_processed["Submission_Date"], errors="coerce")
        df_processed["Submission_Weekday"] = df_processed["Submission_Date"].dt.dayofweek
        
        df_processed["Queue_Category"] = pd.cut(
            df_processed["Queue_Length"],
            bins=[-1, 5, 15, float("inf")],
            labels=["Low", "Medium", "High"]
        )
        
        df_processed["SLA_Breached"] = (
            df_processed["Processing_Days"] > df_processed["SLA_Days"]
        ).astype(int)
        
        needed = ["Queue_Category", "Submission_Weekday", "SLA_Breached"]
        missing_now = [c for c in needed if c not in df_processed.columns]
        
        if missing_now:
            st.error(f"⚠️ Still missing: {', '.join(missing_now)}")
        else:
            st.success("✅ Schema Valid — All columns computed successfully!")
            st.write(f"**SLA_Breached = 1:** {df_processed['SLA_Breached'].sum()}")
            st.write(f"**SLA_Breached = 0:** {(df_processed['SLA_Breached'] == 0).sum()}")
            st.session_state["df"] = df_processed
            st.dataframe(df_processed.head())
    else:
        st.info("👆 Upload your dataset.csv file to begin.")