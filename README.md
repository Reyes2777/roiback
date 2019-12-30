# Roiback

Roiback project by jonathan_reyes. This application manage reservations for customers and employs. find hotels and book the room. This app use [Django Framework](https://www.djangoproject.com/) and [Postgresql](https://www.postgresql.org/)

##Instalation Guide

1. Clone the repo with next run command:
    `git clone git@github.com:Reyes2777/roiback.git`  
2. Create python virtual env, you have two options:
   - virtualenv: `virtualenv roiback -p $(which python3)`
   - virtualenvwrapper: `mkvirtualenv roiback -p $(which python3) -a .`
3. Install dev requirements: `pip install -r requirements_dev.txt`
    
You need create a file .env_server with the next environments:
 
    DEFAULT_DB_HOST=localhost
    DEFAULT_DB_PASSWORD=guest
    DEFAULT_DB_PORT=5432
    DEFAULT_DB_NAME=roiback
    DEFAULT_DB_USER=roiback
    
## Requirements management


There are three requirements files:

1. *requirements_dev.txt* for development.
2. *requirements.txt* for production.

**Please, don't use `pip freeze > requirements[_dev].txt` so we have a cleaner requirements files. Add specific python lib manually instead.**

## Run project

1. `docker-compose up`
2. Open in browser http://localhost:8000