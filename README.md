## Simian

A simple 2D game engine implemented with python, using pygame!

## Especification

- Python v3.6.5
- pygame v1.9.3

## How to setup your environment to contribute to this project

1. Follow these steps on a terminal:

`$ sudo apt-get install python-virtualenv`

`$ mkdir venv`

`$ virtualenv venv/games`

`$ source venv/games/bin/activate`

2. Then go to our simian folder (where you can see setup.py):

`(games) $ python3 setup.py build`

You can also use:

`$ docker-compose -f docker/docker-compose.yml up --build -d `

`$ docker exec -it simian bash`

or get more simple with docker:

`$ make run`

If you're a Vagrant Fanboy, just:

`$ vagrant box add ubuntu/xenial64`

`$ vagrant up`

`$ vagrant ssh`

or get more simple with vagrant:

`$ make v-build`

`$ make v-exec`

-----------------------------------------

And you'll be inside Simian environment!

-------------------------------------------

_**To quit this virtual environment just type:**_

`$ deactivate`
