FROM ubuntu:20.04
USER root
RUN echo "Teste Embedded Edge Agent"
## DEPENDENCIES
RUN apt-get update -yq
RUN apt-get install -yq python3.8
RUN apt-get install -yq python3-pip

## COPING TESTS
WORKDIR /home/test/
COPY  wasm-app/ .
COPY step1.py .
COPY step2.py .

## COPING APLICATION
WORKDIR /home/app
COPY step3.py .
COPY test.py .
COPY wasm-app/ .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python3 test.py

## ENVIRONMENT
ENV DEVICE_ID=61b7709ad019cb6f1ecd088c
ENV ACCESS_KEY=6b497fd4-747f-4594-9e42-af62e7a519ba
ENV ACCESS_SECRET=6aac1ea2ca92c32acd18c933321f71b43316747738b81e7a4bd01fa76be3c2b7