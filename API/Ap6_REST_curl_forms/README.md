# Ap6 – Eigen REST-API experiment met curl (forms)

## Doel
Aantonen dat formuliergegevens (form-data) naar een REST API gestuurd kunnen worden met curl.

## Gebruikte API
- https://httpbin.org/post

## Wat doet dit experiment?
- Met curl wordt een POST request verstuurd.
- De data wordt verzonden als form-data.
- De API stuurt de ontvangen data terug in JSON-formaat.

## Gebruikte curl-commando
```bash
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=burak&category=info"
