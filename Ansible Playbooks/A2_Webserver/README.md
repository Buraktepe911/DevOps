# A2 – Eigen playbook-experiment (webserver)

## Doel
Met Ansible automatisch een webserver (Apache2) installeren en een eigen webpagina uitrollen op de DEVASC VM.
Dit is een “eigen experiment” omdat ik niet enkel installeer, maar ook:
- de service automatisch start + enabled zet
- een eigen `index.html` (A2-pagina) deploy

## Voorwaarden / Context
- Doelhost in deze labomgeving is een lokale “dummy” webserver-IP op de DEVASC VM:
  - `192.0.2.3` (dummy0 interface)
- SSH wordt gebruikt voor Ansible connectie:
  - user: `devasc`
  - pass: `Cisco123!`

## Bestanden in deze folder
- `hosts`  
  Inventory met de target webserver (`192.0.2.3`).
- `ansible.cfg`  
  Config zodat Ansible de lokale `hosts` gebruikt en geen host-key warnings toont.
- `a2_webserver.yaml`  
  Playbook dat Apache2 installeert + service activeert + eigen webpagina plaatst.

## Hoe uitvoeren (run)
Open een terminal en ga naar deze folder:

```bash
cd ~/labs/DevOps/Ansible\ Playbooks/A2_Webserver
