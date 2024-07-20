# Docker

This directory contains the sample web application code and the Dockerfile used to containerize the application.

## Prerequisites

- Docker installed on your local machine.
 
## Install Docker
- Install [Docker Engine](https://docs.docker.com/engine/install/)

## Directory Structure
   ```bash
Decker/
├── app/
|   ├── app.py
|   ├── requirements.txt
|   ├── Dockerfile
└── README.md
   ```
## Sample Web Application
This directory contains a simple Flask web application. Modify the application code as needed.

## Dockerfile

The Dockerfile defines the steps to build a Docker image for the sample web application.

### Build the Docker Image

1. Navigate to the `app/` directory:
   ```bash
   cd ~/Git/AutoDeploymentPipeline/Docker/app
   ```
#### Docker CLI explan: 
- Build the Docker image
   ```bash
   docker build -t ${dockerhub-username}/${app-name}:${tag} .
   ```
- Push the Docker image to Docker Hub:
   ```bash
   docker push ${dockerhub-username}/${app-name}:${tag}
   ```
- Run Docker image on local machine
   ```bash
   docker run -p 5000:5000 ${dockerhub-username}/${app-name}:${tag}
   ```
   -- {tag}: the version of your app
   -- (-p): port 
   