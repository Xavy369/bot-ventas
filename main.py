import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "El bot de Javier Vtas Online está activo y funcionando 24/7.", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Evento recibido:", data)
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
