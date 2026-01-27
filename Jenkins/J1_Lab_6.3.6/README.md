## Jenkins (container) issue op DevASC VM
Jenkins in Docker start niet op deze VM door thread-limieten:
- Java error: `Cannot create VM thread` / `pthread_create failed (EPERM)`
Daarom is de pipeline gedemonstreerd via een shell-script (`pipeline.sh`) met dezelfde CI/CD stappen:
cleanup → build → run → test.

## Demo / Tests
Run de pipeline:
```bash
cd ~/labs/DevOps/Jenkins/J1_Lab_6.3.6
./pipeline.sh
