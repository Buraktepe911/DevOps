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

##Logs bekijken
docker logs dc1-di2


##Laatste regels:

docker logs dc1-di2 --tail 10

##Container betreden (exec)
docker exec -it dc1-di2 /bin/sh


##Binnen de container:

ps aux
exit

##Container stoppen en herstarten
docker stop dc1-di2
docker start dc1-di2


##Controle:

docker ps

##Cleanup (container verwijderen)
docker rm -f dc1-di2


##Controle:

docker ps -a
