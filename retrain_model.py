import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

print("🔄 Building model...")

# Load dataset
df = pd.read_csv("dataset.csv")

# Compute required columns
df["Submission_Date"] = pd.to_datetime(df["Submission_Date"], errors="coerce")
df["Submission_Weekday"] = df["Submission_Date"].dt.dayofweek

df["Queue_Category"] = pd.cut(
    df["Queue_Length"],
    bins=[-1, 5, 15, float("inf")],
    labels=["Low", "Medium", "High"]
)

df["SLA_Breached"] = (df["Processing_Days"] > df["SLA_Days"]).astype(int)

# Features
feature_cols = ["Service_Type", "Priority", "Queue_Category", 
                "Assigned_Office", "Submission_Weekday"]
X = df[feature_cols]
y = df["SLA_Breached"]

# Preprocessing
cat_features = ["Service_Type", "Priority", "Queue_Category", "Assigned_Office"]
preprocessor = ColumnTransformer(
    transformers=[
        ("onehot", OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore"), cat_features)
    ], remainder="passthrough"
)

# Train
model = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("classifier", DecisionTreeClassifier(max_depth=3, random_state=42))
])

model.fit(X, y)

# Save — lalabas na ang file!
joblib.dump(model, "trained_model.joblib")
print(f"✅ SUCCESS! trained_model.joblib created!")
print(f"📊 Total samples: {len(X)} | Breach count: {y.sum()}")