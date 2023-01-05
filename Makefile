# Define the main file
MAIN_FILE = main.py

# Define the requirements file
REQUIREMENTS_FILE = requirements.txt

# Define the Docker image name
DOCKER_IMAGE = stock-trading-bot

# Define the default target
.DEFAULT: help

# Define the help target
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install      Install the required packages"
	@echo "  test         Run the tests"
	@echo "  run          Run the main script"
	@echo "  docker-build  Build the Docker image"
	@echo "  docker-run    Run the Docker container"

# Define the install target
.PHONY: install
install:
	pip install -r $(REQUIREMENTS_FILE)

# Define the test target
.PHONY: test
test:
	python -m pytest

# Define the run target
.PHONY: run
run:
	python $(MAIN_FILE)

# Define the docker-build target
.PHONY: docker-build
docker-build:
	docker build -t $(DOCKER_IMAGE) .

# Define the docker-run target
.PHONY: docker-run
docker-run:
	docker run $(DOCKER_IMAGE)
