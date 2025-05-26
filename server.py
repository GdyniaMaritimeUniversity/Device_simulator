from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Odebrano dane:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
