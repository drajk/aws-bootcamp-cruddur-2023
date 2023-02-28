FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_DEBUG=1
ENV BACKEND_URL=*
ENV FRONTEND_URL=*

EXPOSE ${PORT}

RUN /init.sh
