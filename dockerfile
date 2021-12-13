FROM ubuntu:20.04

RUN echo "Teste Embedded Edge Agent"

WORKDIR /home/app/
COPY  wasm-app/ .
COPY step1.py .