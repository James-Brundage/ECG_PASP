# syntax=docker/dockerfile:1

FROM python:3.7
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt