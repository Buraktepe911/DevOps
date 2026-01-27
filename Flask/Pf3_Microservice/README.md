# Pf3 – Eigen microservice-experiment

## Doel
Dit experiment toont een eigen Flask microservice met meerdere REST endpoints
die JSON data teruggeven.

## Context
- Framework: Flask
- Programmeertaal: Python 3
- Poort: 5051
- Type: REST microservice

## Installatie
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
Starten
python microservice.py
Service draait op:

http://127.0.0.1:5051
Endpoints
/
curl http://127.0.0.1:5051/
/status
curl http://127.0.0.1:5051/status
/info
curl http://127.0.0.1:5051/info
##Conclusie
Deze eigen microservice toont hoe een eenvoudige REST API met Flask wordt
opgezet en getest.
