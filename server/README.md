### What is this?   

Main server side for *@carsurfing* project.
Tasks:
 - manage users (CRUD)
 - request parsing processes
 - DB
 - all bot's alerts

***

### How can I deploy it?
    
 - run `bash deploy_server.sh` to deploy required files for server:
    * local *Composer*
 - run `php -S localhost:2110 src/index.php` to run the server

Required global packages:
 - *PHP 7+*
 - *curl*
    
***

### Docs
[RestAPI url docs](./API_DOC.md)
[RestAPI status docs](./API_RESPONCE_DOC.md)
