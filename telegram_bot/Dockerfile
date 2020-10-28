FROM python:3.9

WORKDIR /app

COPY ["package.json ./", "yarn.lock ./", ".env ./", "requirements.txt ./"]

RUN apt-get update && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt update && \
    apt-get install nodejs -y && \
    apt install yarn -y && \
    yarn && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3 && \
    pip3 install -r requirements.txt

COPY . .

EXPOSE 2305

VOLUME /app

CMD ["python3", "src/index.py"]
