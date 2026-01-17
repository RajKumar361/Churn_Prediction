import sqlite3
from datetime import datetime

DB_PATH = "predictions.db"

def init_db():
    """Initialize the SQLite database and create predictions table if not exists"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT,
            credit_score INTEGER,
            geography TEXT,
            gender TEXT,
            age INTEGER,
            tenure INTEGER,
            balance REAL,
            num_of_products INTEGER,
            has_cr_card INTEGER,
            is_active_member INTEGER,
            estimated_salary REAL,
            prediction TEXT,
            prediction_risk TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_prediction(customer_data, prediction, prediction_risk):
    """Save a single prediction record to the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            customer_id, credit_score, geography, gender, age, tenure, balance,
            num_of_products, has_cr_card, is_active_member, estimated_salary,
            prediction, prediction_risk, timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_data.get("CustomerId"),
        customer_data.get("CreditScore"),
        customer_data.get("Geography"),
        customer_data.get("Gender"),
        customer_data.get("Age"),
        customer_data.get("Tenure"),
        customer_data.get("Balance"),
        customer_data.get("NumOfProducts"),
        customer_data.get("HasCrCard"),
        customer_data.get("IsActiveMember"),
        customer_data.get("EstimatedSalary"),
        prediction,
        prediction_risk,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()


def get_all_predictions():
    """Retrieve all prediction records from the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM predictions ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows
