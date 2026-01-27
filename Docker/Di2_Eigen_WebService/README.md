# Di2 – Eigen image-experiment (web service)

## Doel
Een eigen Flask webservice containerizen met Docker:
- eigen app (JSON endpoints)
- eigen Dockerfile
- image build + container run
- testen via browser en curl

## Build
```bash
docker build -t di2-webservice:1.0 .
Run
docker run -d -p 8081:8081 --name di2-web di2-webservice:1.0
Testen
Browser:

http://127.0.0.1:8081
