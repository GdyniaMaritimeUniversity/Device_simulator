from datetime import datetime
import requests

def send_alert(alert_type, value, device_uuid, url):
    alert_data = {
        "timestamp": datetime.now().isoformat(),
        "device_uuid": device_uuid,
        "type": alert_type,
        "value": value
    }
    try:
        response = requests.post(url, json=alert_data)
        if response.status_code == 200:
            print("🚨 Alert sent successfully.")
        else:
            print(f"⚠️  Alert error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Alert connection error: {e}")

def send_to_api(data, url, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("✔️  Data sent successfully.")
        else:
             print(f"⚠️  API error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error with API: {e}")
