### What is this?   

Telegram bot for *@carsurfing* project.

***

### How can I join it?

 - production bot [link](t.me/carsurfing_bot) or by *@carsurfing_bot* name
 - depelopment (test) bot [link](t.me/challenger_testing_bot) or by *@challenger_testing_bot* name
  - *Heroku* [server url](https://challenger-telegram.herokuapp.com/)

***

### How can I deploy it?

 * ##### Localy

    - run `bash deploy.sh` script to install *Python* virtual environment and all dependencies
    - run `source py_env/bin/activate` to activate virtual environment
    - run `python3 src/index.py` to run bot server

 * ##### On *Heroku*

    - `git push heroku-telegram BRANCH:master`

###### Required global packages:

 * *Python v3+*
 * *pip3*
 * *venv*
    
***

### Docs

[Bot commands](./BOT_COMMANDS.md).
