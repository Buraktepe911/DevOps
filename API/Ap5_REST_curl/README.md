# Ap5 – Eigen REST-API experiment met curl

## Doel
Aantonen dat een REST API getest kan worden met het commando curl.

## Wat doet dit experiment?
- Met curl wordt een HTTP GET request verstuurd naar een publieke REST API.
- De API stuurt een JSON-antwoord terug.
- De JSON-data wordt rechtstreeks weergegeven in de terminal.

Dit toont aan dat een REST API ook getest kan worden zonder Python of een webapp.

## Gebruikte API
- https://api.chucknorris.io/jokes/random

## Gebruikte curl-commando's
```bash
curl https://api.chucknorris.io/jokes/random

curl -X GET https://api.chucknorris.io/jokes/random

curl -i https://api.chucknorris.io/jokes/random
