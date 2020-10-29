FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt
ENV FLASK_APP=src/index.py

COPY . .

EXPOSE 2300

VOLUME /app

CMD ["flask", "run", "--host=0.0.0.0", "--port=2300"]
