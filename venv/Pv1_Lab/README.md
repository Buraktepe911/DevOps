# Pv1 – Python Virtual Environment (Lab-experiment)

## Doel
Het doel van dit experiment is aantonen dat ik correct kan werken met een
Python Virtual Environment (venv):
- een venv aanmaken
- activeren en deactiveren
- Python packages installeren
- een Python script uitvoeren binnen de venv
- werken met requirements.txt

## Context
- Omgeving: DEVASC VM
- Python versie: Python 3
- Virtual environment: .venv

## Stappenplan

### Virtual environment aanmaken
```bash
python3 -m venv .venv
Virtual environment activeren
source .venv/bin/activate
Pip upgraden en package installeren
python -m pip install --upgrade pip
pip install requests
Testscript uitvoeren
python pv1_test.py
Verwacht resultaat:

HTTP statuscode 200

JSON-response van een API
