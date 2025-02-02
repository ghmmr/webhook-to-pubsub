from flask import Flask, request, jsonify
import json
import google.cloud.pubsub_v1 as pubsub
import os

app = Flask(__name__)

# Configurar el cliente de Pub/Sub
project_id = "qwiklabs-gcp-04-0084c53d303b"  # Reemplaza con tu ID de proyecto
topic_id = "transacciones"

publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

@app.route("/", methods=["POST"])
def recibir_datos():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No se recibió JSON"}), 400

        # Publicar en Pub/Sub
        message_json = json.dumps(data).encode("utf-8")
        future = publisher.publish(topic_path, message_json)
        future.result()

        return jsonify({"status": "Mensaje enviado a Pub/Sub"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
