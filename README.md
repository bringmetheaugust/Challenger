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

:pushpin:All link are for production.
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
   <summary>📔How deployed mulltiapp <i>Heroku</i></summary>
   <ul>
      <li><code>heroku create challenger-telegram</code></li>
      <li><code>git remote rename heroku heroku-telegram</code></li>
      <li><code>heroku create challenger-server --buildpack https://github.com/heroku/heroku-buildpack-multi-procfile.git
</code></li>
      <li><code>git remote rename heroku heroku-server</code></li>
   </ul>
</details>

Be my Challenger!
