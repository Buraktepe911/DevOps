# A3 – Eigen playbook-experiment 2 (andere server)

## Doel
Dit experiment toont het gebruik van een **andere server** met Ansible.
In plaats van Apache (A2) wordt hier **Nginx** gebruikt als webserver.

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
- a3_nginx_server.yaml  
  Playbook voor installatie en configuratie van Nginx.
- README.md  
  Documentatie en teststappen.

## Wat doet het playbook?
Het playbook voert automatisch de volgende stappen uit:
1. Stopt Apache (poort 80 vrijmaken)
2. Installeert Nginx
3. Start en activeert de Nginx service
4. Plaatst een eigen HTML-pagina via Ansible

## Playbook uitvoeren
Ga naar de juiste map:

```bash
cd ~/labs/DevOps/Ansible\ Playbooks/A3_AndereServer
Run het playbook:

ansible-playbook -v a3_nginx_server.yaml
Testen / Verificatie
Test 1 – Browser test
Open Chromium en ga naar:

http://192.0.2.3
Verwacht resultaat:

Titel: A3 - Nginx Webserver

Tekst: Deze pagina is uitgerold met Ansible.

Test 2 – Service status
Controleer of Nginx draait:

sudo systemctl status nginx
Verwacht:

active (running)

Test 3 – Curl test
Test via terminal:

curl http://192.0.2.3
## Opmerking over A3 en A2 (belangrijk)
A3 gebruikt **Nginx** als webserver, terwijl A2 **Apache** gebruikt.
Beide services gebruiken standaard **poort 80** en kunnen daarom niet
tegelijk actief zijn.

Als A3 getest wordt **na A2**, moet Apache eerst gestopt worden.

Gebruik hiervoor de volgende commando’s:

```bash
sudo systemctl stop apache2
sudo systemctl disable apache2
sudo systemctl start nginx
sudo systemctl enable nginx
