# XENETA TASK

## Prerequisites

Docker engine

## Python libraries

flask: micro web framework for building web applications in Python. It provides tools, libraries, and resources to help developers build scalable and maintainable web applications.

psycopg2-binary: provides a PostgreSQL database adapter for the Python programming language

pytest: testing framework for Python that helps developers write and run unit tests

## Docker Setup

For postgresql, Dockerfile are in `db` folder

For Flask, Dockerfile are in `root` folder

## Docker Compose

Docker compose is user for container orchestration

## Commands

To setup db and run the service
`docker-compose up -d db`

To run the unit tests
`docker-compose run pythonapp pytest`

To run the flask app
`docker-compose up --build pythonapp`

To cleanup the container
`docker-compose down`

### CI/CD

Github action for Test and Lint

## Outputs

Please use postman json collection to try the api after all the docker app is running

![Output](https://github.com/ashishyd/xeneta-task/blob/main/Screenshot%202023-03-25%20at%2012.08.46%20PM.png)
