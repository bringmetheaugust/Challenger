FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .env ./

RUN pip3 install -r requirements.txt
ENV FLASK_APP=src/index.py

EXPOSE 2300

VOLUME /app

CMD ["flask", "run", "--host=0.0.0.0", "--port=2300"]
