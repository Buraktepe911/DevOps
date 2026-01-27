# J1 – Jenkins Pipeline Experiment (Lab 6.3.6)

## Doel
Aantonen dat het CI/CD pipeline-concept begrepen en uitgevoerd kan worden:
- build
- run
- test
- cleanup  
Dit gebeurt met Docker en een Flask-app.

---

## Context (DevASC VM beperking)
De Jenkins Docker container kon **niet starten** op de DevASC VM door systeembeperkingen:

- Java VM error:  
  `Cannot create VM thread`  
  `pthread_create failed (EPERM)`
- Oorzaak: beperkte thread/resources op de VM

➡️ Daarom is de pipeline **gedemonstreerd via een shell-script** (`pipeline.sh`)  
dat **exact dezelfde stappen uitvoert** als een Jenkins pipeline.

Dit is een **functionele en geldige workaround** voor deze omgeving.

---

## Gebruikte applicatie
- Flask webapp
- Draait in Docker container
- Endpoint:
  - `/` → bevestigingstekst

Voorbeeld output: http://127.0.0.1:5050

