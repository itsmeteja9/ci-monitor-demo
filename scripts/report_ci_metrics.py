import sys
import requests
import os
from datetime import datetime

DATADOG_API_KEY = os.getenv("DATADOG_API_KEY")

def send_event(status):
    title = "GitHub CI Run"
    text = f"CI job completed with status: {status}"
    alert_type = "error" if status != "success" else "success"

    response = requests.post(
        "https://api.datadoghq.com/api/v1/events",
        headers={"DD-API-KEY": DATADOG_API_KEY},
        json={
            "title": title,
            "text": text,
            "alert_type": alert_type,
            "tags": ["ci-monitoring", f"status:{status}"]
        }
    )
    print(f"Sent event: {response.status_code} - {response.text}")

if __name__ == "__main__":
    status = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    send_event(status)
