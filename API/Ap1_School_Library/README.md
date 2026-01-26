# Ap1 – School Library API (Lab 4.5.5)

## Doel
Het testen van een REST API met verschillende tools:
- Swagger / OpenAPI
- curl
- Postman
- Python script

## API info
- Base URL: http://library.demo.local/api/v1
- Docs: http://library.demo.local/api/v1/docs

## Geteste endpoints
- GET /books
- GET /books/{id}
- POST /loginViaBasic
- POST /books
- DELETE /books/{id}

## Authenticatie
- Basic Auth (cisco / Cisco123!)
- API Key via header: X-API-KEY

## curl
```bash
curl http://library.demo.local/api/v1/books
curl "http://library.demo.local/api/v1/books?includeISBN=true"

