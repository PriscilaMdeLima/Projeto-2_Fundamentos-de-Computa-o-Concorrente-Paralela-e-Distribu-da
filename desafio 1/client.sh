#!/bin/sh

echo "Cliente iniciando requisições..."

while true; do
    curl -s http://server:8080
    echo ""
    sleep 5
done
