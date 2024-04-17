FROM python:3.8.13-slim-bullseye

WORKDIR /app
ENV ELEVENLABS_API_KEY=ELEVENLABS_API_KEY


#OPENAI

ENV OPENAI_API_KEY=API_KEY

RUN apt-get -y update  && apt-get install -y

RUN pip install --upgrade setuptools 

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000:8000


CMD uvicorn server:app --host 0.0.0.0 --port 8000