# Pv2 – Python Virtual Environment (Deployment)

## Doel
Dit experiment toont een eigen deployment met Python en een virtual
environment. Een Flask webapplicatie draait binnen een venv.

## Context
- Omgeving: DEVASC VM
- Python versie: Python 3
- Framework: Flask
- Virtual environment: .venv
- Poort: 5000

## Setup

### Virtual environment aanmaken
```bash
python3 -m venv .venv
Virtual environment activeren
source .venv/bin/activate
Flask installeren
pip install flask
Applicatie starten
python app.py
Testen / Verificatie
Browser test
Open Chromium en ga naar:

http://127.0.0.1:5000
Verwacht resultaat:

Pv2 deployment OK - Flask draait in venv!
