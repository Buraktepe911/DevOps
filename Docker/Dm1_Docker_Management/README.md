# Dm1 – Docker management experiment

## Doel
Aantonen dat Docker correct beheerd kan worden:
- containers & images
- logs & monitoring
- inspect (config/details)
- networks
- volumes
- cleanup

---

## Voorbereiding (container voor demo)
Dm1 gebruikt een bestaande webservice container (Di2).
Start de container voor demo (als die nog niet draait):

```bash
docker run -d -p 8082:8081 --name dc1-di2 di2-webservice:1.1
docker ps

## 1) Containers & images overzicht
docker ps
docker ps -a
docker images

## 2) Inspect (container details)
docker inspect dc1-di2 | head -n 40

## 3) Monitoring (CPU/RAM)
docker stats --no-stream

## 4) Logs beheren
docker logs dc1-di2 --tail 50

## 5) Exec
docker exec -it dc1-di2 /bin/sh
ps aux
exit

## 6) Networks
docker network ls

## 7) Volumes demo
docker volume create dm1-data
docker run --rm -v dm1-data:/data busybox sh -c "echo Dm1_OK > /data/test.txt && cat /data/test.txt"

## 8) Cleanup
docker rm -f dc1-di2
docker volume rm dm1-data

(Extra demo: logs genereren door requests te doen)

curl http://127.0.0.1:8082/api/status
curl http://127.0.0.1:8082/api/status
docker logs dc1-di2 --tail 10
