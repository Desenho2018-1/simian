#!/bin/bash

# Represents the latest version of the project according to setup.py file
VERSION=$(python setup.py --version)

echo "Latest Simian version is $VERSION";

# double validation in script and in .travis.yml
if [[ "${TRAVIS_BRANCH}" == "master" ]]; then
	echo "Deploying to Docker registry latest Simian...";
	docker login -e "$DOCKER_EMAIL" -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD";
	docker build -f docker/Dockerfile -t simian:"$VERSION" .;
	docker tag alaxalves/simian:"$VERSION";
	docker push alaxalves/simian:"$VERSION";
else
	echo "Skipping Docker registry deploy";
fi;
