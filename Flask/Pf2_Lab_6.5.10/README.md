# Pf2 – Logon-page experiment (Lab 6.5.10)

## Doel
Dit experiment toont de evolutie van wachtwoordbeveiliging in een Flask
microservice:
1. Onveilige opslag van wachtwoorden in plaintext
2. Veiligere opslag met hashing (SHA-256)

Het verschil tussen beide methodes wordt aangetoond met tests.

## Context
- Omgeving: DEVASC VM
- Framework: Flask
- Programmeertaal: Python 3
- Database: SQLite
- Poort: 5000
- Protocol: HTTPS (self-signed certificaat)

## Bestanden
- password_evolution.py  
  Flask applicatie met plaintext en hashed login.
- test.db  
  SQLite database met gebruikers.

---

## Applicatie starten
```bash
python3 password_evolution.py
De service draait op:

https://127.0.0.1:5000
Testen / Verificatie
Algemene test
curl -k https://127.0.0.1:5000/
Verwacht:

Pf2 - Password evolution is running!
Fase 2 – Plaintext passwords (onveilig)
Signup (plaintext)
curl -k -X POST https://127.0.0.1:5000/signup_plaintext -d "username=test&password=1234"
Login correct
curl -k -X POST https://127.0.0.1:5000/login_plaintext -d "username=test&password=1234"
Login fout
curl -k -X POST https://127.0.0.1:5000/login_plaintext -d "username=test&password=fout"
Plaintext in database (onveilig)
sqlite3 test.db "SELECT username, password FROM users_plaintext;"
Fase 3 – Hashed passwords (veiliger)
Signup (hashed)
curl -k -X POST https://127.0.0.1:5000/signup_hashed -d "username=test2&password=abcd"
Login correct
curl -k -X POST https://127.0.0.1:5000/login_hashed -d "username=test2&password=abcd"
Login fout
curl -k -X POST https://127.0.0.1:5000/login_hashed -d "username=test2&password=fout"
Hashed passwords in database
sqlite3 test.db "SELECT username, password_hash FROM users_hashed;"
