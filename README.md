## Simian

[![codecov](https://codecov.io/gh/Desenho2018-1/simian/branch/master/graph/badge.svg)](https://codecov.io/gh/Desenho2018-1/simian)

A simple 2D game engine implemented with python, using pygame!

Get to know us better at: https://desenho2018-1.github.io/simian/

## Dependencies

You should have installed:
- Python v3.6.5 

## How to setup your environment to contribute to this project
Follow these steps on a terminal to create a virtualenv:

`$ python3.6 -m venv env`

`$ source env/bin/active`

Then go to our simian folder (where you can see setup.py):

`(env) $ pip install -r requirements.txt`

`(env) $ python setup.py build`

And you ready to run simian!

## Setup sample game

Inside simian folder, run:

`$ simian startproject`

Simian will ask you some parameters, leave them empty and a demo __pong__ game will be created. After that go to the **pong** folder and run the sample:

`$ cd pong/`

`$ simian run`

Then you're running your first game using simian. 

_**To quit this virtual environment just type:**_

`$ deactivate`
