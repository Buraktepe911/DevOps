# A2 – Eigen playbook-experiment (webserver)

## Doel
Dit experiment toont hoe met Ansible automatisch een **Apache webserver**
wordt geïnstalleerd en geconfigureerd, inclusief het uitrollen van een
**eigen webpagina**.

## Context
- Omgeving: DEVASC VM
- Doel-IP: 192.0.2.3 (dummy0 interface)
- Ansible connectie via SSH:
  - gebruiker: devasc
  - wachtwoord: Cisco123!

## Bestanden in deze map
- hosts  
  Inventory met de target webserver.
- ansible.cfg  
  Lokale Ansible configuratie.
- a2_webserver.yaml  
  Playbook dat Apache installeert en een eigen HTML-pagina plaatst.
- README.md  
  Documentatie en teststappen.

## Wat doet het playbook?
Het playbook voert automatisch de volgende stappen uit:
1. Installeert Apache2 via apt
2. Start de Apache service
3. Zorgt dat Apache automatisch start bij boot (enabled)
4. Plaatst een eigen HTML-pagina in `/var/www/html/index.html`

## Playbook uitvoeren
Ga naar de juiste map:

```bash
cd ~/labs/DevOps/Ansible\ Playbooks/A2_Webserver
Run het playbook:

ansible-playbook -v a2_webserver.yaml
Testen / Verificatie
Test 1 – Browser test
Open Chromium en ga naar:

http://192.0.2.3
