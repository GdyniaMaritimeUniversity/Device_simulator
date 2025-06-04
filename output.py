import requests

headers = {
    "Authorization": "Bearer 5R3661N"
}

def send_to_api(data, url):
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("✔️  Data sent successfully.")
        else:
             print(f"⚠️  API error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error with API: {e}")
        
