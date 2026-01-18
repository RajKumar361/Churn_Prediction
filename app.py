from flask import Flask, render_template, request
import pickle
import numpy as np
from prediction_db import init_db, save_prediction, get_all_predictions

# Flask configuration
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# ----------------------------
# Initialize Database
# ----------------------------
try:
    init_db()
    print(" Database initialized successfully.")
except Exception as e:
    print(f"Database init error: {e}")

# ----------------------------
# Load Model Artifacts
# ----------------------------
try:
    MODEL_PATH = "models/churn_model.pkl"
    SCALER_PATH = "models/scaler.pkl"
    FEATURES_PATH = "models/features.pkl"

    model = pickle.load(open(MODEL_PATH, "rb"))
    scaler = pickle.load(open(SCALER_PATH, "rb"))
    feature_order = pickle.load(open(FEATURES_PATH, "rb"))

    print(" Model, Scaler, and Features loaded successfully.")
except Exception as e:
    print(f" Model loading failed: {e}")
    model = None
    scaler = None
    feature_order = []

# ----------------------------
# Risk Classification
# ----------------------------
def get_risk_category(prob):
    if prob >= 0.7:
        return "High"
    elif prob >= 0.4:
        return "Medium"
    else:
        return "Low"

# ----------------------------
# Home Page (Single Page App)
# ----------------------------
@app.route("/")
def index():
    try:
        records = get_all_predictions()
        total = len(records)

        high = len([r for r in records if r[13] == "High"]) if total else 0
        medium = len([r for r in records if r[13] == "Medium"]) if total else 0
        low = len([r for r in records if r[13] == "Low"]) if total else 0
    except:
        total = high = medium = low = 0

    return render_template(
        "index.html",
        total=total,
        high=high,
        medium=medium,
        low=low,
        probability=None,
        risk=None
    )

# ----------------------------
# Prediction Route
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if model is None or scaler is None:
        return "Model or scaler not loaded."

    try:
        form_data = request.form.to_dict()

        # Initialize all features with 0
        features = dict.fromkeys(feature_order, 0)

        # Numeric fields
        features["CreditScore"] = float(form_data["CreditScore"])
        features["Age"] = float(form_data["Age"])
        features["Tenure"] = float(form_data["Tenure"])
        features["Balance"] = float(form_data["Balance"])
        features["NumOfProducts"] = float(form_data["Product"])
        features["EstimatedSalary"] = float(form_data["EstimatedSalary"])

        features["HasCrCard"] = int(form_data.get("HasCrCard", 1))
        features["IsActiveMember"] = int(form_data.get("IsActiveMember", 1))

        # Gender Encoding
        if form_data["Gender"] == "Male" and "Gender_Male" in features:
            features["Gender_Male"] = 1

        # Geography Encoding
        country = form_data["Country"]
        if country == "Germany" and "Geography_Germany" in features:
            features["Geography_Germany"] = 1
        elif country == "Spain" and "Geography_Spain" in features:
            features["Geography_Spain"] = 1

        # Model prediction
        X = np.array([features[f] for f in feature_order]).reshape(1, -1)
        X_scaled = scaler.transform(X)

        prob = model.predict_proba(X_scaled)[0][1]
        probability_percent = round(prob * 100, 2)
        risk = get_risk_category(prob)

        # Save to DB
        customer_data = {
            "CustomerId": form_data.get("CustomerId", "N/A"),
            "CreditScore": features["CreditScore"],
            "Geography": country,
            "Gender": form_data["Gender"],
            "Age": features["Age"],
            "Tenure": features["Tenure"],
            "Balance": features["Balance"],
            "NumOfProducts": features["NumOfProducts"],
            "HasCrCard": features["HasCrCard"],
            "IsActiveMember": features["IsActiveMember"],
            "EstimatedSalary": features["EstimatedSalary"]
        }

        save_prediction(customer_data, f"{probability_percent}%", risk)

        # Reload stats
        records = get_all_predictions()
        total = len(records)
        high = len([r for r in records if r[13] == "High"])
        medium = len([r for r in records if r[13] == "Medium"])
        low = len([r for r in records if r[13] == "Low"])

        return render_template(
            "index.html",
            probability=probability_percent,
            risk=risk,
            total=total,
            high=high,
            medium=medium,
            low=low
        )

    except Exception as e:
        return f" Prediction Error: {e}"

# ----------------------------
# Run Server
# ----------------------------
if __name__ == "__main__":
    print(" Flask server is starting...")
    app.run(host="0.0.0.0", port=5000, debug=True)
