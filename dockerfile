FROM ubuntu:20.04
USER root

RUN echo "Teste Embedded Edge Agent"

RUN apt-get update -yq
RUN apt-get install -yq python3.8
RUN apt-get install -yq python3-pip

WORKDIR /home/test/
COPY  wasm-app/ .
COPY step1.py .
COPY step2;py .
COPY requirements.txt .

WORKDIR /home/app

COPY step3.py .
COPY wasm-app/ .