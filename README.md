# Measurement Device Simulator (Python)

This project is a simulator of a device that generates measurements of temperature, humidity, pressure, and light level, then sends the data to a specified API in JSON format.

## 🔧 Requirements

- Python 3.8+
- `pip` (Python package manager)

## 📦 Installation

1. Clone the repository or download the project files.

2. Install required packages:
3. 
```bash
pip install -r requirements.txt
```

## 🚀 Running the Simulator

```bash
python simulator.py
```

When launching, provide the API endpoint (e.g., http://localhost:5000/api/data) and the interval (in seconds) for how often the measurements should be generated and sent.

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
  "timestamp": "2025-05-26T15:22:05.123456",
  "temperature": 23.5,
  "humidity": 45.2,
  "pressure": 1012.3,
  "light": 567.8
}
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
