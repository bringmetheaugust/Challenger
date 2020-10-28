FROM node:13.6

WORKDIR /app

COPY package.json ./
COPY yarn.lock ./

RUN yarn

COPY . .

EXPOSE 2101

VOLUME /app

CMD ["yarn", "dev"]
