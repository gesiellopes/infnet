FROM python:3.12.9-slim

RUN apt-get update && \
    apt-get install -y build-essential \
    && apt-get install openjdk-17-jre -y\
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8888 4040

CMD jupyter lab --port-retries=0 --ip 0.0.0.0 --allow-root --IdentityProvider.token="" --ServerApp.password=""