# FROM python:3.9-slim

# WORKDIR /app

# COPY . /app

# RUN pip install -r requirements.txt

# CMD ["python3", "scripts/generate_report.py"]

FROM jenkins/jenkins:lts

USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip

USER jenkins
