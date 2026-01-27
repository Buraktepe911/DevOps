# Ap3 – Eigen API-experiment (Python)

## Doel
Een externe publieke REST API gebruiken in Python en JSON verwerken.

## Beschrijving
Dit script maakt gebruik van de **Chuck Norris Jokes API**.
Het verstuurt een GET request, ontvangt een JSON-response en leest
verschillende velden uit zoals:
- joke tekst
- id
- categorie
- created_at

De informatie wordt overzichtelijk in de terminal weergegeven.

## Bestand
- chuck_norris_api.py

## Run
```bash
pip3 install requests
python3 chuck_norris_api.py
