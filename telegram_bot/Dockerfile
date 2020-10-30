FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .env ./

RUN apt-get update && \
    apt-get install nodejs -y && \
    apt-get install npm -y && \
    npm install -g nodemon -y && \
    pip3 install -r requirements.txt

VOLUME /app/src

CMD ["nodemon", "--exec", "python3", "./src/index.py"]
