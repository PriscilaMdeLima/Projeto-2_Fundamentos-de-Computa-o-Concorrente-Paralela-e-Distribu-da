#!/bin/sh
# O nome 'server' é o nome do serviço no docker-compose, que é resolvido na rede Docker.
SERVER_URL="http://server:8080"

echo "Iniciando cliente de requisições para $SERVER_URL..."

while true; do
    echo "---"
    echo "Enviando requisição para $SERVER_URL..."
    curl -s $SERVER_URL
    echo ""
    sleep 5
done
