import streamlit as st

def run_sad_module():
    st.header("5. System Design — SAD Integration")
    
    st.subheader("Functional Requirements")
    st.markdown("""
    | ID | Requirement | Status |
    |----|-------------|--------|
    | FR1 | Upload & validate CSV dataset | ✅ Implemented |
    | FR2 | Display data preview & statistics | ✅ Implemented |
    | FR3 | Generate EDA visualizations | ✅ Implemented |
    | FR4 | Predict SLA breach risk | ✅ Implemented |
    | FR5 | Show performance dashboard | ✅ Implemented |
    | FR6 | Display system design & workflow | ✅ Implemented |
    """)
    
    st.subheader("Non-Functional Requirements")
    st.markdown("""
    - **Performance:** Page loads under 3 seconds; prediction under 1 second
    - **Usability:** Clear labels, guidance messages, consistent layout
    - **Reliability:** Input validation, error handling, fallback messages
    - **Privacy:** No external data sharing; all processing local
    """)
    
    st.subheader("System Workflow")
    st.code("Upload CSV → Validate → Preview → Analyze → Predict → Dashboard", language="text")
    
    st.subheader("Data Flow Diagram")
    st.info("""
    **DFD Level 0 Overview:**
    - **External Entity:** User / Administrator
    - **Process:** SLA Monitoring & Prediction System
    - **Data Store:** Uploaded CSV Dataset + Trained Model
    - **Output:** Predictions, Visualizations, Reports
    """)