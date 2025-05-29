# Measurement Device Simulator (Python)

A sensor device simulator for testing a backend API. Supports data generation, measurement sending, alerting, and concurrent simulation of multiple devices.

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

You'll be asked for:

- 🔗 **API base URL**, e.g.: `http://localhost:5000/api`
- ⏱️ **Measurement interval** in seconds
- 🔁 **Number of devices** to simulate concurrently

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
├── uuid_resolver.py   # Retrieves UUID using MAC address
├── requirements.txt   # Package list
└── README.md          # Documentation
```

## 📡 Backend API – Required Endpoints

Your backend should expose:

### GET `/uuid?mac={mac}`

Returns the UUID assigned to a device's MAC address.

**Response:**

```json
{
  "uuid": "a1b2c3d4-e5f6-7890-abcd-1234567890ef"
}
```

---

### POST `/data`

Receives sensor measurements.

**Example payload:**

```json
{
  "timestamp": "2025-05-29T12:00:00+00:00",
  "device_uuid": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
  "temperature": 25.3,
  "humidity": 45.7,
  "pressure": 1012.5
}
```

---

### POST `/alerts`

Sends alerts, e.g., for high temperature.

**Example:**

```json
{
  "timestamp": "2025-05-29T12:00:00+00:00",
  "device_uuid": "a1b2c3d4-e5f6-7890-abcd-1234567890ef",
  "type": "high_temperature",
  "value": 30.2
}
```

---

## 📌 Author

Test project for educational purposes – IoT simulation using Python.

---

### 📄 `requirements.txt`

```txt
requests
flask
```

---
