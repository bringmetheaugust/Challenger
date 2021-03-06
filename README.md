# Challenger🚙


![online](https://img.shields.io/website?url=http://challenger.ua) ![license](https://img.shields.io/github/license/bringmetheaugust/Challenger) ![releaze](https://img.shields.io/github/v/release/bringmetheaugust/Challenger) ![realise date](https://img.shields.io/github/release-date/bringmetheaugust/Challenger) ![issues](https://img.shields.io/github/issues-raw/bringmetheaugust/Challenger) ![PR](https://img.shields.io/github/issues-pr-raw/bringmetheaugust/Challenger)

***

<div align="center">
<h3><b>📣PROJECT IS FROZEN</b></h3>
it doesn't work at the moment, all description is not actual
</div>

***

## Description

Bots for searching cars on all ukrainians automobile commerce platforms.
After a few simple steps, bot subscribes Your on search and sends to You every new car models wich You have chosen.

## How can I join it?

 * ![Telegram](https://img.shields.io/badge/-telegram-000?&logo=telegram)
    - join bot by [link](t.me/carsurfing_bot) or find him by *@carsurfing_bot* name
    - type `/start` for running the bot

 * ![Viber](https://img.shields.io/badge/-Viber-000?&logo=viber)
    - join bot by [link](lol.lol) or find him by *@carsurfing_bot* name
    - type `/go` to start new search

:pushpin:All link are only for production.    
:pushpin:Development links are on the same **Docs**.

## How can I deploy this?

 * ##### Localy by Docker🐋

    - `docker-compose up --no-start` to deploy containers
    - `docker-compose start` to up containers

 * ##### Remotely by Heroku

    Run `bash heroku_multiapp_deploy.sh` or deploy each modules separately.    
    All deploying steps for each module descibed in the same **Docs**.
    

:pushpin:By default, each module runs on test domains. All test domains described in the same **Docs**.    
:pushpin:Some domains (bot tokens), which described on `.env` files, are hidden by `.gitignore` for our safity. Dont forget to add them before deploying.

## Docs

 * Main docs

   - [main server](./server/README.md)
      * [api docs](./server/API_DOC.md)

   - [telegram bot](./telegram_bot/README.md)
      * [bot commands](./telegram_bot/BOT_COMMANDS.md)

 * Heroku data

   * ![Telegram](https://img.shields.io/badge/-telegram-000?&logo=telegram)
      - url: <a>https://challenger-telegram.herokuapp.com</a></li>
      - git remote server name: <code>heroku-telegram</code></li>
      - git remote: <code>https://git.heroku.com/challenger-telegram.git</code></li>
      - *Heroku* name: <code>challenger-telegram</code></li>

   * ![server](https://img.shields.io/badge/-server-000?&logo=node.js)
      - url: <a>https://challenger-server.herokuapp.com</a></li>
      - git remote server name: <code>heroku-server</code></li>
      - git remote <code>https://git.heroku.com/challenger-server.git</code>
      - *Heroku* name: <code>challenger-server</code></li>

## WTF?

<details>
   <summary>📔How to deploy <i>Heroku</i> mulltiapp in monorepo</summary>
   <ul>
      <li><b>build app</b>
         <ul>
            <li><code>heroku create APP_NAME --remote REMOTE_NAME</code></li>
            <li><code>heroku buildpacks:add --app APP_NAME BUILDPACK</code></li>
         </ul>
      </li>
      <li><b>add buildpack to manage multiapps in monorepo</b>
         <ul>
            <li><code>heroku buildpacks:add --app APP_NAME https://github.com/lstoll/heroku-buildpack-monorepo -i 1</code></li>
            <li><code>heroku config:set --app APP_NAME APP_BASE=APP_ROOT_PATH</code></li>
         </ul>
      </li>
      <li><b>add buildpack for saparate Procfile for each app</b>
         <ul>
            <li><code>heroku buildpacks:add --app APP_NAME heroku-community/multi-procfile -i 2</code></li>
            <li><code>heroku config:set --app APP_NAME PROCFILE=PROCFILE_PATH</code></li>
         </ul>
      </li>
   </ul>
</details>
