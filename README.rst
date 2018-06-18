======
Simian
======

Simian is a framework thats provides a game engine using pygame.

==============
Especification
==============

Python: v3.6.5
pygame: v1.9.3

Quick Start
-----------

1. Follow these steps on a terminal::

    $ sudo apt-get install python-virtualenv

    $ mkdir venv

    $ virtualenv venv/games

    $ source venv/games/bin/activate


2. Then go to the project's root::

    (games) $ python3 setup.py build

3. After that your can use either docker/makefile abstraction to run your simian environment

**To quit this virtual environment just type:**

$ deactivate

=================
Setup sample game
=================

Inside simian folder, run:

    $ simian startproject

Simian will ask you some parameters then a sample game will be created. After that go to the pong folder and run the sample:

    $ cd pong/

    $ simian run

====
PyPi
====

A more stable version of the package is in: https://pypi.org/project/simian-engine/