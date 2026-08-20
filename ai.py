import requests
import os


N8N_WEBHOOK_URL = os.getenv("N8N_HIGH_RISK_WEBHOOK",
    "https://arjhun0216.app.n8n.cloud/webhook-test/Smart_Student_Prediction")

def send_student_details(name, student_id, attendance, study_hours, internal_marks, assignment, previous_score, result, risk , recommendation):
    data = {
        "name": name,
        "student_id": student_id,
        "attendance": attendance,
        "study_hours": study_hours,
        "internal_marks": internal_marks,
        "assignment": assignment,
        "previous_score": previous_score,
        "prediction": result,
        "risk": risk,
        "recommendation": recommendation
    }

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=data)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error sending data to n8n: {e}")