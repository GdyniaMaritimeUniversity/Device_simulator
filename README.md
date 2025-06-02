# Measurement Device Simulator (Python)

This project is a simulator of a devices that generates measurements of temperature, humidity, pressure, and light level, then sends the data to a specified API in JSON format.

## 🔧 Requirements

- Python 3.8+
- `pip` (Python package manager)

## 📦 Installation

1. Clone the repository or download the project files.

2. Install required packages:

```bash
pip install -r requirements.txt
```

## 🚀 Running the Simulator

```bash
python simulator.py
```

You will be prompted to:

Enter the API endpoint URL (e.g., http://localhost:5000/api/data),
Enter the interval in seconds between measurements,
Enter the number of devices to simulate.

Each simulated device sends its own data periodically, including a unique MAC address. Occasionally, extreme values will be generated to simulate alerts.

## 🧪 Optional Test API Server

You can run a simple Flask server to receive the data:

```bash
python server.py
```

Your server.py file should contain:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Data received:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```

## 📁 Project Structure

```
Device_simulator/
├── simulator.py       # Main simulator application
├── sensors.py         # Simulated sensors
├── output.py          # Sending data to API
├── server.py          # Test API server (Flask)
├── requirements.txt   # Package list
└── README.md          # Documentation
```

## ✅ Sample JSON Data Sent to the API

```json
{
  "timestamp": "2025-06-02T16:03:11.012345",
  "temperature": 52.8,
  "humidity": 93.5,
  "pressure": 1055.4,
  "mac_address": "00:16:3e:00:00:05",
  "alerts": [
    {
      "alert_name": "High Temperature",
      "description": "Temperature exceeded 50°C: 52.8°C"
    },
    {
      "alert_name": "High Humidity",
      "description": "Humidity exceeded 90%: 93.5%"
    },
    {
      "alert_name": "High Pressure",
      "description": "Pressure exceeded 1050 hPa: 1055.4 hPa"
    }
  ]
}
```

If no alerts are triggered, alerts will be an empty array:

```json
  "alerts": []
```

## 📌 Author

Test project for educational purposes – IoT simulation using Python.

---

### 📄 `requirements.txt`

```txt
requests
flask
```

---
