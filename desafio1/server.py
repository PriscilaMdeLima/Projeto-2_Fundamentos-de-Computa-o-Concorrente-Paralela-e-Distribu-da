from flask import Flask, request
import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    client_ip = request.remote_addr
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] Hello from Server! Received request from {client_ip}"
    print(message) # Log para o console do container
    return message, 200

if __name__ == '__main__':
    # Roda o servidor na porta 8080 e acessível externamente (0.0.0.0)
    app.run(host='0.0.0.0', port=8080)
