FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y build-essential \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY api.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install "fastapi[standard]"

EXPOSE 8000

CMD fastapi run api.py --host 0.0.0.0