FROM python:3.11-slim

WORKDIR /app

# Minder kans op "can't start new thread" tijdens install
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1 PIP_PROGRESS_BAR=off

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir --progress-bar off -r requirements.txt

COPY app.py .

EXPOSE 8081

CMD ["python3", "app.py"]
