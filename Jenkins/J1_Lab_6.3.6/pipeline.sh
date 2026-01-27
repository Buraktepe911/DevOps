#!/usr/bin/env bash
set -e

echo "=== J1 Pipeline (zonder Jenkins) ==="
echo "[1/4] Cleanup oude container"
docker rm -f j1-running 2>/dev/null || true

echo "[2/4] Build Docker image"
docker build -t j1-sampleapp .

echo "[3/4] Run container"
docker run -d -p 5050:5050 --name j1-running j1-sampleapp

echo "[4/4] Test (curl + check tekst)"
curl -s http://127.0.0.1:5050 | grep "J1 Jenkins Pipeline OK"

echo "✅ Pipeline OK"
