#!/bin/bash

# 1) tempdir structuur
mkdir -p tempdir/templates tempdir/static

# 2) files kopiëren
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# 3) Dockerfile genereren
echo "FROM python:3.11-slim" > tempdir/Dockerfile
echo "ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1 PIP_PROGRESS_BAR=off" >> tempdir/Dockerfile
echo "RUN python -m pip install --upgrade pip" >> tempdir/Dockerfile
echo "RUN pip install --no-cache-dir --progress-bar off flask" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

# 4) image build
cd tempdir
docker build -t sampleapp .

# 5) container run
docker run -t -d -p 8080:8080 --name samplerunning sampleapp

# 6) toon containers
docker ps -a
