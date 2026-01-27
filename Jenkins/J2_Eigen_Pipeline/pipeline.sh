#!/usr/bin/env bash
set -e

echo "=== J2 Eigen Pipeline (Di2 webservice) ==="

echo "[1/5] Cleanup oude container"
docker rm -f j2-di2 2>/dev/null || true

echo "[2/5] Build image (Di2)"
cd /home/devasc/labs/DevOps/Docker/Di2_Eigen_WebService
docker build -t di2-webservice:j2 .

echo "[3/5] Run container"
docker run -d -p 8090:8081 --name j2-di2 di2-webservice:j2

echo "[4/5] Test API endpoints"
curl -s http://127.0.0.1:8090/api/status | grep -i running
curl -s "http://127.0.0.1:8090/api/echo?msg=j2" | grep -i j2

echo "[5/5] Success"
echo "✅ J2 pipeline OK"
