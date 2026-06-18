# Flask Color App

A simple Flask web application that changes the background color of the page based on the `APP_COLOR` environment variable.

## Features

* Reads the `APP_COLOR` environment variable.
* Changes the page background color accordingly.
* Uses `white` as the default color if `APP_COLOR` is not set.
* Containerized using Docker.

## Requirements

* Python 3.13
* Flask
* Docker Desktop

## Run Locally

1. Clone the repository.

2. Install dependencies:

pip install -r requirements.txt

3. Run the application:

python app.py

4. Open:

http://localhost:5000

## Environment Variables

| Variable  | Description                  | Default |
| --------- | ---------------------------- | ------- |
| APP_COLOR | Background color of the page | white   |

Example:

APP_COLOR=red

## Run with Docker

Build the image:

docker build -t flask-color-app .

Run the container:

docker run -e APP_COLOR=green -p 5000:5000 flask-color-app

This project uses a lightweight Docker base image: python:3.13-slim

Open:

http://localhost:5000

## Project Structure

flask-color-app/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── Dockerfile
└── .dockerignore


## Authors

-Samikshaa
-Nasrin

