# Pf1 – Flask-experiment (gebaseerd op lab 6.3.6)

## Doel
Dit experiment is gebaseerd op lab 6.3.6 en toont hoe een eenvoudige
Flask webapplicatie wordt gestart en getest.
De applicatie gebruikt templates en static bestanden.

## Context
- Omgeving: DEVASC VM
- Framework: Flask
- Programmeertaal: Python 3
- Poort: 5050 (gekozen om conflicten met andere services te vermijden)

## Bestanden in deze map
- sample_app.py  
  Flask applicatie uit het lab.
- templates/  
  HTML templates gebruikt door Flask.
- static/  
  Statische bestanden (CSS, afbeeldingen).

## Installatie (venv)
In deze map wordt een Python virtual environment gebruikt.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
Applicatie starten
Start de Flask applicatie met:

python sample_app.py
De applicatie draait nu op:

http://127.0.0.1:5050
Testen / Verificatie
Test 1 – Browser test
Open Chromium en ga naar:

http://127.0.0.1:5050
Verwacht resultaat:

Webpagina met tekst:
“You are calling me from 127.0.0.1”
