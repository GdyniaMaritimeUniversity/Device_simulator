import time
import threading
from datetime import datetime
import sensors
import output

def generate_mac_address(index):
    base_mac = [0x00, 0x16, 0x3e,
                (index >> 16) & 0xff,
                (index >> 8) & 0xff,
                index & 0xff]
    return ':'.join(map(lambda x: f"{x:02x}", base_mac))

def check_alerts(data):
    alerts = []

    if data["temperature"] > 50:
        alerts.append({
            "alert_name": "High Temperature",
            "description": f"Temperature exceeded 50°C: {data['temperature']}°C"
        })

    if data["humidity"] > 90:
        alerts.append({
            "alert_name": "High Humidity",
            "description": f"Humidity exceeded 90%: {data['humidity']}%"
        })

    if data["pressure"] > 1050:
        alerts.append({
            "alert_name": "High Pressure",
            "description": f"Pressure exceeded 1050 hPa: {data['pressure']} hPa"
        })

    return alerts


def generate_measurement(mac_address):
    data = {
        "timestamp": datetime.now().isoformat(),
        "temperature": sensors.read_temperature(),
        "humidity": sensors.read_humidity(),
        "pressure": sensors.read_pressure(),
        "mac_address": mac_address
    }
    data["alerts"] = check_alerts(data)
    return data


def simulate_device(device_id, api_url, interval):
    mac_address = generate_mac_address(device_id)
    while True:
        data = generate_measurement(mac_address)
        print(f"[{mac_address}] Data: {data}")
        output.send_to_api(data, api_url)
        time.sleep(interval)

def main():
    api_url = input("Enter API URL (e.g., http://localhost:5000/api/data): ").strip()
    interval = float(input("Enter interval (seconds): "))
    num_devices = int(input("Enter number of devices to simulate: "))
    print(f"\nStarting simulation with {num_devices} device(s)...\n(Press Ctrl+C to stop)\n")

    threads = []
    try:
        for i in range(num_devices):
            t = threading.Thread(target=simulate_device, args=(i, api_url, interval), daemon=True)
            threads.append(t)
            t.start()

        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
