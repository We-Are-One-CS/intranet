# We Are One (CentraleSupélec)

GitHub repository for our member website. This repository contains all files needed to see and integrate in the original website the 4 functionnalities discussed during the initial phase of the project. 
The project is currently in development. Started at CentraleSupélec with Lattitude and We Are One.

## Getting Started

### Prerequisities 

Install Docker : 

* [Windows install](https://docs.docker.com/docker-for-windows/install/)
* [Mac install](https://docs.docker.com/docker-for-mac/install/)
* [Linux install](https://www.docker.com/community-edition)

Make sure **Docker** is installed and works : 
```bash 
$ docker --version
Docker version 19.03.5, build 633a0ea
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Run the project

Clone the project on your machine and chdir: 
```bash
$ git clone git@github.com:We-Are-One-CS/intranet.git
$ cd intranet/
```
Build the image: 
```bash 
$ docker build .
```

Migrate the database: 

```bash
$ docker-compose run web python /code/manage.py makemigrations

$ docker-compose run web python /code/manage.py migrate --noinput
```

Create an admin user: 

```bash
$ docker-compose run web python /code/manage.py createsuperuser
```

Run the app in a Docker container: 

```bash
$ docker-compose up -d --build
```

Now you should see the app by taping http://127.0.0.1:8000 in your web browser. 


When you're done, don't forget to close down your Docker container : 

```bash
$ docker-compose down
```

## Functionnalities
1. Personal data page: Each user has an unique page for seeing its private data. The users have the possibility to change their information.
2. Events page: This page will show all the events that We Are One organize, and any user or visitor is able to subscribe to WAO events. There are public and private events, free and non-free event as well.
3. Self development programs offered by We Are One: The website has the possibility to show all self development programs that the user can search and interact, either by subscribing or by setting its interest.
4. Users directory: This functionnality is mainly to being able to see the users database. Each user (that has the right to see) will be able to see the contact of others users.

## To go further
todo

## Authors
- Matheus Elyasha LOPES
- Leïla Bekaddour
