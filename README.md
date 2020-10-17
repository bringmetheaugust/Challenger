### What is this?   
Bots for searching cars on all automobile commerce platforms.
After a few simple staps, bot subscribes Your on search and sends to You every new car models wich You have chosen.

***

### How can I join it?

 * ##### Telegram🏄🏻
    - join bot by [link](t.me/carsurfing_bot) or find him by *@carsurfing_bot* name
    - type `/start` for running the bot

 * ##### Viber💩
    - join bot by [link](lol.lol) or find him by *@carsurfing_bot* name
    - type `/go` to start new search

:pushpin:All link are only for production.
:pushpin:Development links are on the same **Docs**.

***

### How can I deploy it?

 * ##### Localy (each module separately)

    All deploying steps for each module descibed in the same **Docs**.

 * ##### Localy by Docker🐋

    - run `bash deploy_by_docker.sh` to deploy containers
    - run `bash run_by_docker.sh` to run containers

 * ##### Remotely by Heroku

    - 
    

:pushpin:By default, each module runs on test domains. All test domains described in the same **Docs**.
:pushpin:Some domains (bot tokens), which described on `.env` files, are hidden by `.gitignore` for our safity. Dont forget to add them before deploying.

***

### Docs

##### Main docs

   - [main server](./server/README.md)
      * [api docs](./server/API_DOC.md)
      * [api responce doc](./server/API_RESPONCE_DOC.md)

   - [telegram bot](./telegram_bot/README.md)
      * [bot commands](./telegram_bot/BOT_COMMANDS.md)

   - [site parser](./parser/README.md)

##### Heroku data

   * **Telegram**🏄🏻
      - url: <a>https://challenger-telegram.herokuapp.com</a></li>
      - git remote server name: <code>heroku-telegram</code></li>
      - git remote: <code>https://git.heroku.com/challenger-telegram.git</code></li>
      - *Heroku* name: <code>challenger-telegram</code></li>

    * **Server**👑
      - url: <a>https://challenger-server.herokuapp.com</a></li>
      - git remote server name: <code>heroku-server</code></li>
      - git remote <code>https://git.heroku.com/challenger-server.git</code>
      - *Heroku* name: <code>challenger-server</code></li>

***

### Who made this?
August Luzanovsky, 2020

***

### WTF?

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

Be my Challenger!
