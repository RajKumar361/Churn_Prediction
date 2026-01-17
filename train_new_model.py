import pandas as pd
import numpy as np
import pickle
import json
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Paths
os.makedirs("models", exist_ok=True)
DATA_PATH = "churn.csv"
MODEL_PATH = os.path.join("models", "model.pkl")
SCALER_PATH = os.path.join("models", "scaler.pkl")
FEATURES_PATH = os.path.join("models", "features.json")

print("📂 Loading dataset...")
df = pd.read_csv(DATA_PATH)
print(f"✅ Dataset loaded: {df.shape}")

# Fix column names (strip spaces)
df.columns = df.columns.str.strip()

# Target column
target = "Exited"

if target not in df.columns:
    raise ValueError(f"Target column '{target}' not found in dataset!")

# Drop unused columns
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# Encode categorical variables
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)

X = df.drop(target, axis=1)
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
print("🧠 Training model...")
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
score = model.score(X_test_scaled, y_test)
print(f"✅ Model accuracy: {score*100:.2f}%")

# Save model, scaler, features
os.makedirs("models", exist_ok=True)
pickle.dump(model, open("models/churn_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(list(X.columns), open("models/features.pkl", "wb"))

print("✅ Model, Scaler, and Features saved successfully in /models")