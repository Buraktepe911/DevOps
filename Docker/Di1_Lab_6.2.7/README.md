# Di1 – Lab 6.2.7 (Sample Web App in Docker)

## Doel
Een Flask webapplicatie in een Docker container bouwen en uitvoeren.
Het lab gebruikt een bash script dat:
- een tijdelijke buildmap maakt (tempdir)
- bestanden kopieert (app + templates + static)
- een Dockerfile genereert
- een Docker image bouwt
- een container start met port mapping
- testen uitvoert via browser/curl

## Bestanden
- sample_app.py
- templates/
- static/
- sample-app.sh (bouwt image en start container)

## Belangrijke aanpassing (VM probleem)
Tijdens het lab was er een fout: `RuntimeError: can't start new thread`.
Daarom:
- Docker base image gezet op `python:3.11-slim`
- pip progress bar uitgeschakeld in Dockerfile
- Flask run ingesteld op `threaded=False`

## Run (build + start container)
```bash
bash ./sample-app.sh
Controle
docker ps
Verwacht:

container samplerunning

poort mapping 0.0.0.0:8080->8080/tcp

Testen / Verificatie
Browser test
Open Chromium:

http://127.0.0.1:8080

Curl test
curl -i http://127.0.0.1:8080
Verwacht: HTTP 200 OK + HTML output.
