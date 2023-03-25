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