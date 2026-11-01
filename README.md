## 📊 Use Case Diagram

```mermaid
graph TB
    User[User / Admin]
    
    User -->|uses| UC1
    User -->|views| UC2
    User -->|explores| UC3
    User -->|runs| UC4
    User -->|checks| UC5
    User -->|reviews| UC6
    
    subgraph SLA_Breach_Prediction_System
        UC1[Upload & Validate Dataset]
        UC2[View Data Preview & Info]
        UC3[Explore Data Visualizations]
        UC4[Predict SLA Breach Risk]
        UC5[View Performance Dashboard]
        UC6[View System Design & Requirements]
    end
