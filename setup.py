from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

CLASSIFIERS= [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: Portuguese",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

META_FILE = read(META_PATH)

def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()

def find_meta(meta):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))

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

    classifiers=CLASSIFIERS,

    license=find_meta('license'),

    keywords='',

    author='',

    author_email='',

    maintainer='',

    maintainer_email='',
)
