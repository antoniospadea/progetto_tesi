from flask import Flask, jsonify, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/start_container', methods=['POST'])
def start_container():
    try:
        # Avvia il container se non è già in esecuzione
        container = client.containers.run(
            "analizzatore-energetico",
            detach=True,
            ports={'8000/tcp': 8000},
            name="analizzatore_container"
        )
        return jsonify({'message': f"Container {container.short_id} avviato"}), 200
    except docker.errors.APIError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stop_container', methods=['POST'])
def stop_container():
    try:
        container = client.containers.get("analizzatore_container")
        container.stop()
        container.remove()
        return jsonify({'message': f"Container {container.short_id} fermato e rimosso"}), 200
    except docker.errors.NotFound:
        return jsonify({'error': 'Container non trovato'}), 404
    except docker.errors.APIError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/status_container', methods=['GET'])
def status_container():
    try:
        container = client.containers.get("analizzatore_container")
        status = container.status
        return jsonify({'container_id': container.short_id, 'status': status}), 200
    except docker.errors.NotFound:
        return jsonify({'error': 'Container non trovato'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
