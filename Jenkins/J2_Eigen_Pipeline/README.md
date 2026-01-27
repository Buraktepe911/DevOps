# J2 – Eigen pipeline-experiment

## Doel
Eigen CI/CD pipeline (pipeline as code) voor een Docker webservice (Di2):
- build
- run
- test
- cleanup

## Context
Op deze DevASC VM kon Jenkins container niet starten door thread-limieten (Java VM).
Daarom wordt de pipeline:
- gedemonstreerd via `pipeline.sh`
- en als Jenkins Pipeline code opgeslagen in `Jenkinsfile`.

## Pipeline uitvoeren (demo)
```bash
cd ~/labs/DevOps/Jenkins/J2_Eigen_Pipeline
./pipeline.sh
Testen
API status:

curl http://127.0.0.1:8090/api/status
