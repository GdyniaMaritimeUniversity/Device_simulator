import requests

def send_to_api(data, url):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("✔️  Dane wysłane pomyślnie.")
        else:
            print(f"⚠️  Błąd API: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Błąd połączenia z API: {e}")
