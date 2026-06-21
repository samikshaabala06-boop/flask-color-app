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

CI/CD pipeline configured using GitHub Actions.

## AWS Deployment

The Docker image was pushed to Amazon Elastic Container Registry (ECR) and deployed on an Amazon EC2 instance.

### AWS Services Used

* Amazon ECR for storing Docker images
* Amazon EC2 for hosting the application
* Security Groups for allowing HTTP access

### ECR Repository

064123638482.dkr.ecr.us-east-1.amazonaws.com/flask-color-app

### Deployment Steps

1. Created an EC2 instance using Amazon Linux 2023.
2. Installed Docker on the EC2 instance.
3. Configured AWS CLI on the EC2 instance.
4. Logged in to Amazon ECR.
5. Pulled the Docker image from ECR.
6. Ran the Docker container using:

sudo docker run -d -e APP_COLOR=green -p 80:5000 064123638482.dkr.ecr.us-east-1.amazonaws.com/flask-color-app:latest

7. Accessed the application through the EC2 Public IPv4 address.

---

## CI/CD Pipeline

GitHub Actions was configured to automate Docker image creation and publishing.

### Workflow

Git Push
→ GitHub Actions
→ Build Docker Image
→ Login to Amazon ECR
→ Tag Docker Image
→ Push Docker Image to ECR

### Workflow File

.github/workflows/deploy.yml

### Current Status

The workflow automatically builds the Docker image and pushes it to Amazon ECR whenever code is pushed to the main branch.



## Authors

- Samikshaa
- Nasrin