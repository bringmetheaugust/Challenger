### What is this?   

Main server for *@carsurfing* project.
##### Tasks:

 - manage users (CRUD)
 - request parsing processes
 - DB
 - all bot's alerts

***

### How can I deploy it?
    
 * ##### Localy

   - run `bash local_deploy.sh` to install required packages by local *Composer*
   - run `bash local_run.sh` to run the server

 * ##### On *Heroku*

   - `git push heroku-server BRANCH:master`

###### Required global packages:

 - *PHP 7+*
 - *curl*
 - *php-xml*
    
***

### Docs

[RestAPI url docs](./API_DOC.md).
[RestAPI status docs](./API_RESPONCE_DOC.md).
