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
