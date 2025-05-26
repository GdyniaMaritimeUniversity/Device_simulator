import time
from datetime import datetime
import sensors
import output

def generate_measurement():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": sensors.read_temperature(),
        "humidity": sensors.read_humidity(),
        "pressure": sensors.read_pressure(),
        "light": sensors.read_light_level()
    }

def main():
    api_url = input("Podaj URL API (np. http://localhost:5000/api/data): ").strip()
    interval = float(input("Podaj interwał (sekundy): "))
    print("Start symulacji z wysyłką do API...\n(Ctrl+C aby zakończyć)\n")

    try:
        while True:
            data = generate_measurement()
            print("Dane:", data)
            output.send_to_api(data, api_url)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSymulacja zakończona.")

if __name__ == "__main__":
    main()
