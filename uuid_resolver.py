import uuid
import requests

def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])

def fetch_uuid(api_base_url):
    mac = get_mac_address()
    try:
        response = requests.get(f"{api_base_url}/uuid?mac={mac}")
        if response.status_code == 200:
            return response.json().get("uuid")
        else:
            print(f"⚠️ UUID fetch error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ UUID fetch failed: {e}")
    return None
