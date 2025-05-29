import time
from datetime import datetime
import sensors
import output

def generate_measurement():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": sensors.read_temperature(),
        "humidity": sensors.read_humidity(),
        "pressure": sensors.read_pressure()
    }

def main():
    api_url = input("Enter API URL (e.g., http://localhost:5000/api/data): ").strip()
    interval = float(input("Enter interval (seconds): "))
    print("Starting simulation with data being sent to API...\n(Press Ctrl+C to stop)\n")

    try:
        while True:
            data = generate_measurement()
            print("Data:", data)
            output.send_to_api(data, api_url)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
