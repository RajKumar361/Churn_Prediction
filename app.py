from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
from datetime import datetime
from prediction_db import init_db, save_prediction, get_all_predictions

app = Flask(__name__)

# Initialize the local SQLite database
init_db()

# Load trained model, scaler, and feature order
try:
    MODEL_PATH = "models/churn_model.pkl"
    SCALER_PATH = "models/scaler.pkl"
    FEATURES_PATH = "models/features.pkl"

    model = pickle.load(open(MODEL_PATH, "rb"))
    scaler = pickle.load(open(SCALER_PATH, "rb"))
    feature_order = pickle.load(open(FEATURES_PATH, "rb"))

    print("[INFO] Model, Scaler, and Feature List Loaded Successfully.")
except Exception as e:
    print(f"[ERROR] Could not load model/scaler/features: {e}")
    model = None
    scaler = None
    feature_order = []

# ----------------------------
# Risk Classification Function
# ----------------------------
def get_risk_category(prob):
    if prob >= 0.7:
        return "High"
    elif prob >= 0.4:
        return "Medium"
    else:
        return "Low"

# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict_form")
def predict_form():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or scaler is None:
        return "Model or Scaler not loaded properly."

    form_data = request.form.to_dict()

    # Extract and preprocess input data
    try:
        features = {
            "CreditScore": float(form_data["CreditScore"]),
            "Gender": int(form_data["Gender"]),
            "Age": float(form_data["Age"]),
            "Tenure": float(form_data["Tenure"]),
            "Balance": float(form_data["Balance"]),
            "NumOfProducts": float(form_data["Product"]),
            "HasCrCard": int(form_data["HasCrCard"]),
            "IsActiveMember": int(form_data["IsActiveMember"]),
            "EstimatedSalary": float(form_data["EstimatedSalary"]),
            "Geography": float(form_data["Country"])
        }

        # Convert into model input array
        X = np.array([features[f] for f in feature_order]).reshape(1, -1)
        X_scaled = scaler.transform(X)
        prob = model.predict_proba(X_scaled)[0][1]
        probability_percent = round(prob * 100, 2)
        risk = get_risk_category(prob)

        # Save prediction to DB
        customer_data = {
            "CustomerId": form_data.get("CustomerId", "N/A"),
            "CreditScore": features["CreditScore"],
            "Geography": features["Geography"],
            "Gender": "Male" if features["Gender"] == 1 else "Female",
            "Age": features["Age"],
            "Tenure": features["Tenure"],
            "Balance": features["Balance"],
            "NumOfProducts": features["NumOfProducts"],
            "HasCrCard": features["HasCrCard"],
            "IsActiveMember": features["IsActiveMember"],
            "EstimatedSalary": features["EstimatedSalary"]
        }

        save_prediction(customer_data, f"{probability_percent}%", risk)

        return render_template(
            "result.html",
            probability=probability_percent,
            risk=risk
        )

    except Exception as e:
        return f"Error while predicting: {e}"

@app.route("/stats")
def stats():
    records = get_all_predictions()
    total = len(records)
    if total == 0:
        return render_template("stats.html", total=0)

    high = len([r for r in records if r[13] == "High"])
    medium = len([r for r in records if r[13] == "Medium"])
    low = len([r for r in records if r[13] == "Low"])

    # Extract probabilities safely
    probs = []
    for r in records:
        try:
            val = float(r[12].replace("%", ""))
            probs.append(val)
        except:
            pass

    avg_prob = round(sum(probs) / len(probs), 2) if probs else 0

    # Format for display
    recent = [
        {"timestamp": r[14], "probability": r[12], "risk": r[13]}
        for r in records[:10]
    ]

    return render_template(
        "stats.html",
        total=total,
        high=high,
        med=medium,
        low=low,
        avg_prob=avg_prob,
        recent=recent
    )

if __name__ == "__main__":
    app.run(debug=True)
