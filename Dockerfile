FROM python:3.13-alpine

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./travel_agent/*.py ./travel_agent/

