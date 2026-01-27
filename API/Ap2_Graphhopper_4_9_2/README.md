# Ap2 – Graphhopper REST API in Python (Lab 4.9.2)

## Doel
Een externe REST API (Graphhopper) integreren in een Python applicatie.

## Functionaliteit
- Geocoding: plaats → latitude/longitude
- Routing: afstand en reistijd berekenen
- Turn-by-turn directions
- Keuze van voertuig (car, bike, foot)

## Bestanden
- graphhopper_parse-json_1.py t/m graphhopper_parse-json_7.py
- graphhopper_parse-json_7.py is de eindversie

## Werking (kort)
1) Start- en bestemmingslocatie ingeven
2) Geocoding API haalt coördinaten op
3) Route API berekent afstand en tijd
4) Richtingsinstructies worden getoond

## Run
```bash
cd ~/labs/devnet-src/graphhopper
python3 graphhopper_parse-json_7.py
