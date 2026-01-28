# Di2 – Eigen Docker Image Experiment (Web Service)

## Doel
Een eigen Docker image bouwen voor een Python Flask webservice.

---

## Beschrijving
Deze webservice is geschreven in Python (Flask) en wordt verpakt
in een Docker image via een zelfgemaakte Dockerfile.

De service exposeert API endpoints die gebruikt worden in latere experimenten.

---

## Gebruikte technologie
- Python 3
- Flask
- Docker

---

## Build image
```bash
cd ~/labs/DevOps/Docker/Di2_Eigen_WebService
docker build -t di2-webservice:1.1 .
Run container
docker run -d -p 8081:8081 --name di2-web di2-webservice:1.1
Testen
API status
curl http://127.0.0.1:8081/api/status
