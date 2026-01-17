import pandas as pd
import numpy as np
import pickle
import json
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Paths & folders
# -----------------------------
DATASET_PATH = "churn.csv"

os.makedirs("models", exist_ok=True)
os.makedirs("data", exist_ok=True)

MODEL_PATH = "models/churn_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURES_PATH = "models/features.pkl"

# -----------------------------
# Load dataset
# -----------------------------
print("📂 Loading dataset...")
df = pd.read_csv(DATASET_PATH)
print(f"✅ Dataset loaded: {df.shape}")

# Fix column names
df.columns = df.columns.str.strip()

# -----------------------------
# Target column
# -----------------------------
target = "Exited"

if target not in df.columns:
    raise ValueError(f"❌ Target column '{target}' not found in dataset!")

# -----------------------------
# Drop unused columns
# -----------------------------
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# -----------------------------
# Encode categorical variables
# -----------------------------
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)

# -----------------------------
# Split features & target
# -----------------------------
X = df.drop(target, axis=1)
y = df[target]

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Save split datasets ✅ NEW
# -----------------------------
X_train.to_csv("data/X_train.csv", index=False)
X_test.to_csv("data/X_test.csv", index=False)
y_train.to_csv("data/y_train.csv", index=False)
y_test.to_csv("data/y_test.csv", index=False)

print("📁 Train/Test data saved in 'data/' folder")

# -----------------------------
# Feature scaling
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# Train model
# -----------------------------
print("🧠 Training model...")
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X_train_scaled, y_train)

# -----------------------------
# Evaluate model
# -----------------------------
score = model.score(X_test_scaled, y_test)
print(f"✅ Model accuracy: {score * 100:.2f}%")

# -----------------------------
# Save model artifacts
# -----------------------------
pickle.dump(model, open(MODEL_PATH, "wb"))
pickle.dump(scaler, open(SCALER_PATH, "wb"))
pickle.dump(list(X.columns), open(FEATURES_PATH, "wb"))

print("✅ Model, Scaler, and Features saved successfully in /models")
