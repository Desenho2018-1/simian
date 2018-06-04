from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='simian_engine',

    version='0.0.1',

    description='A simple 2D game engine implemented with python!',

    url='https://github.com/Desenho2018-1/simian',

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'simian']),

    install_requires=['pygame==1.9.3'],

    entry_points={
        'console_scripts': [
            'simian = simian.cli.cmd:main',
        ],
    },
)
