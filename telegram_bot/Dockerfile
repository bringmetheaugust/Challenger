FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt update && \
    apt-get install nodejs -y && \
    apt-get install npm -y && \
    npm install -g nodemon -y && \
    pip3 install -r requirements.txt

COPY . .

VOLUME /app

CMD ["nodemon", "--exec", "python3", "./src/index.py"]
