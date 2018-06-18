from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

import codecs
from os import path
import os

here = path.abspath(path.dirname(__file__))

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: Portuguese",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements('requirements.txt', session='hack')

# reqs is a list of requirement
REQUIRES = [str(ir.req) for ir in INSTALL_REQS]

setup(
    name='simian_engine',

    version='0.0.3',

    description='A simple 2D game engine implemented with python!',

    long_description=codecs.open('README.rst', 'rb', 'utf8').read(),

    url='https://github.com/Desenho2018-1/simian',

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'simian']),

    install_requires=REQUIRES,

    entry_points={
        'console_scripts': [
            'simian = simian.cli.cmd:main',
        ],
    },

    classifiers=CLASSIFIERS,

    license='MIT',

    keywords=['game', 'engine', 'simian'],

    author='Simian',

    author_email='simiangameengine@gmail.com',

    maintainer='Simian',

    maintainer_email='simiangameengine@gmail.com',

    platforms='any',
)
