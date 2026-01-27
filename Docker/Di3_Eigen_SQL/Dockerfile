FROM python:3.11-slim

WORKDIR /app

# SQLite zit standaard in Python, geen extra install nodig
COPY db_app.py .

# Run script (maakt DB + doet SELECT)
CMD ["python3", "db_app.py"]
