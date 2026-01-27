# Dc1 – Run Containers Experiment

## Doel
Aantonen dat Docker containers correct kunnen worden:
- gestart
- getest
- beheerd (logs, exec, stop/start)
- opgeruimd

Voor dit experiment wordt de **Di2 eigen webservice container** gebruikt.

---

## Gebruikte image
- Image: `di2-webservice:1.1`
- Type: Python Flask webservice
- Interne poort: `8081`
- Externe poort: `8082`

---

## Container starten
```bash
docker run -d -p 8082:8081 --name dc1-di2 di2-webservice:1.1
Controle:

docker ps
Testen (verificatie)
Test 1 – Browser
Open in Chromium:

http://127.0.0.1:8082
Test 2 – API status (curl)
curl http://127.0.0.1:8082/api/status
Verwacht resultaat:

JSON met service-naam, status en tijd
