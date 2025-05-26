# Symulator Urządzenia Pomiarowego (Python)

Ten projekt to symulator urządzenia, które generuje pomiary temperatury, wilgotności, ciśnienia oraz poziomu światła, a następnie wysyła dane do zdefiniowanego API w formacie JSON.

## 🔧 Wymagania

- Python 3.8+
- `pip` (Python package manager)

## 📦 Instalacja

1. Sklonuj repozytorium lub pobierz pliki projektu.

2. Zainstaluj wymagane pakiety:

```bash
pip install -r requirements.txt
```

## 🚀 Uruchomienie symulatora

```bash
python simulator.py
```

Podczas uruchamiania podaj adres API (np. `http://localhost:5000/api/data`) i interwał (w sekundach), co ile mają być generowane i wysyłane dane.

## 🧪 Opcjonalny serwer API do testów

Możesz uruchomić prosty serwer Flask do odbioru danych:

```bash
python server.py
```

Plik `server.py` powinien zawierać:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Odebrano dane:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```

## 📁 Struktura projektu

```
Device_simulator/
├── simulator.py       # Główna aplikacja
├── sensors.py         # Symulowane czujniki
├── output.py          # Wysyłanie danych do API
├── server.py          # Testowy serwer AP (Flask)
├── requirements.txt   # Lista pakietów
└── README.md          # Dokumentacja
```

## ✅ Przykładowe dane wysyłane do API

```json
{
  "timestamp": "2025-05-26T15:22:05.123456",
  "temperature": 23.5,
  "humidity": 45.2,
  "pressure": 1012.3,
  "light": 567.8
}
```

## 📌 Autor

Projekt testowy do celów edukacyjnych – symulacja IoT z Pythonem.

---

### 📄 `requirements.txt`

```txt
requests
flask
```

---
