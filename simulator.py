import time
from datetime import datetime
import sensors
import output
from concurrent.futures import ThreadPoolExecutor
from uuid_resolver import fetch_uuid

def generate_measurement(device_uuid):
    return {
        "timestamp": datetime.now().isoformat(),
        "device_uuid": device_uuid,
        "temperature": sensors.read_temperature(),
        "humidity": sensors.read_humidity(),
        "pressure": sensors.read_pressure()
    }

def device_simulation(api_url, alert_url, interval):
    uuid = fetch_uuid(api_url)
    if not uuid:
        print("❌ UUID not found, stopping device.")
        return

    try:
        while True:
            data = generate_measurement(uuid)
            print("Data:", data)
            output.send_to_api(data, api_url + "/data")

            if data["temperature"] > 28.0:
                output.send_alert("high_temperature", data["temperature"], uuid, alert_url)

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nDevice simulation stopped.")

def main():
    api_url = input("Enter base API URL (e.g., http://localhost:5000/api): ").strip()
    alert_url = api_url + "/alerts"
    interval = float(input("Enter interval (seconds): "))
    device_count = int(input("How many devices to simulate in parallel? "))

    print(f"Starting simulation for {device_count} device(s)...\n")

    with ThreadPoolExecutor(max_workers=device_count) as executor:
        for _ in range(device_count):
            executor.submit(device_simulation, api_url, alert_url, interval)

if __name__ == "__main__":
    main()
