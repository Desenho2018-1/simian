FROM python:3.6

LABEL Maintainers=simiangameengine@gmail.com
LABEL Version=0.0.3

RUN apt-get update && \
    apt-get install -y python3 build-essential python3-pip python3-dev && \
    apt-get install -y libsdl-image1.2-dev libsdl-mixer1.2-dev && \
    apt-get install -y libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion && \
    apt-get install -y libportmidi-dev libfreetype6-dev libavformat-dev libswscale-dev mercurial

COPY ./././ /home/simian/

WORKDIR /home/simian/

RUN pip3 install -r requirements.txt

RUN python3 setup.py build
