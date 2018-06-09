build:
	@echo "\nBuilding your Simian environment..."
	@docker build -f scripts/docker/Dockerfile -t simian .
	@echo "\nDONE\n"	

exec:
	@echo "\nExecuting your Simian environment..."
	@docker-compose -f scripts/docker/docker-compose.yml up -d
	@docker exec -it simian /bin/bash
	@echo "\nDONE\n"

run:
	@echo "\nRunning/Re-mounting your Simian environment..."
	@docker-compose -f scripts/docker/docker-compose.yml up --build -d
	@docker exec -it simian /bin/bash
	@echo "\nDONE\n"

test:
	@echo "\nRunning Simian tests..."
	@docker exec -it simian /bin/bash -c "python3 -m pytest"
	@echo "\nDONE\n"

install:
	@echo "\nInstalling Simian dependencies..."
	@docker exec -it simian /bin/bash -c "pip3 install -r requirements.txt"
	@echo "\nDONE\n"

rm:
	@echo "\nRemoving Simian's docker container!..."
	@docker rm simian
	@echo "\nDONE\n"	

rm-network:
	@echo "\nRemoving Simian's docker network!..."
	@docker network rm simian-network
	@echo "\nDONE\n"

rmi:
	@echo "\nRemoving Simian's docker image!..."
	@docker rmi simian

help:
	@echo "\n\t\t\t\tSimian"
	@echo "\n\tmake build - Builds the docker image that contains the app"
	@echo "\tmake run - Runs the previously created docker image and enters the container"
	@echo "\tmake rm - Removes the container created by the app"
	@echo "\tmake rm-network - Removes the default network created by the app"
	@echo "\tmake help - Outputs this list\n"
