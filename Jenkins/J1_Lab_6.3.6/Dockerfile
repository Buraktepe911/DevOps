FROM python:3.11-slim

WORKDIR /app
COPY app.py .

# FIX: vermijd pip progress-bar (threads) op deze VM
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_PROGRESS_BAR=off

RUN python -m pip install --upgrade pip
RUN pip install --progress-bar off flask

EXPOSE 5050
CMD ["python3", "app.py"]
