![Django CI](https://github.com/We-Are-One-CS/intranet/workflows/Django%20CI/badge.svg)
# We Are One (CentraleSupélec)

GitHub repository for our member website. This repository contains all files needed to see and integrate in the original website the 4 functions discussed during the initial phase of the project. 
The project is currently in development. Started at CentraleSupélec with Lattitude and We Are One.

## Getting Started

### Prerequisites 


1. `Django 2.2.10` 
2. [`Python 3.7.4`](https://www.python.org/downloads/release/python-374/)
3. [`PostgreSQL 10`](https://www.postgresql.org/download/)
3. For others requirements, see `requirements.txt`

## Run the project

Clone  the project on your machine and change the directory : 
```bash
$ git clone git@github.com:We-Are-One-CS/intranet.git
$ cd intranet/
```

Migrate the database: 

```bash
$ python manage.py makemigrations core 

$ python manage.py migrate --noinput
```

Create an admin user: 

```bash
$ python manage.py createsuperuser
```

Run the app in a Django server: 

```bash
$ python manage.py runserver
```

Now you should see the app by taping http://127.0.0.1:8000 in your web browser. 


When you're done, don't forget to exit the server by : 

```bash
Quit the server with CTRL-BREAK
(In Windows) Ctrl + C
```

## Functions
1. Personal data page: Each user has an unique page for seeing its private data. The users have the possibility to change their information.
2. Events page: This page will show all the events that We Are One organize, and any user or visitor is able to subscribe to WAO events. There are public and private events, free and non-free event as well.
3. Self development programs offered by We Are One: The website has the possibility to show all self development programs that the user can search and interact, either by subscribing or by setting its interest.
4. Users directory: This function is mainly to being able to see the users database. Each user (that has the right to see) will be able to see the contact of others users.

## To go further



## Authors
- Leïla Bekaddour
- Matheus Elyasha LOPES
- Vítor ALBUQUERQUE MARANHÃO RIBEIRO
- Ali Raïki
- Yvan Lanore
