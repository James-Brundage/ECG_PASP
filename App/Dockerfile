# syntax=docker/dockerfile:1

FROM python:3.7
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --progress-bar off --upgrade pip
# Update system and install git and git-lfs
# RUN apt-get update && \
#     apt-get install -y git git-lfs && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache-dir -r requirements.txt