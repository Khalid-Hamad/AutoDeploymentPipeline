# Automated Deployment Pipeline

## Overview

This repository contains the code and configurations for a complete automated deployment pipeline for a containerized web application. The pipeline utilizes Ansible for configuration management, Docker for containerization, and Kubernetes for orchestration.

## Repository Structure
```bash
AutoDeploymentPipeline
├── ansible/
│   ├── playbooks/
│   │   ├── docker_build_push.yaml
│   │   ├── k8s_deploy.yaml
|   └── README.md
├── Decker/
|   ├── app/
│   |   ├── app.py
│   |   ├── requirements.txt
│   |   ├── Dockerfile
|   └── README.md
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
|   └── README.md
└── README.md
```
- `ansible/`: Contains Ansible playbooks for automating Docker image build/push and Kubernetes deployment.
- `app/`: Contains the sample web application code, Dockerfile, and requirements.
- `k8s/`: Contains Kubernetes manifests for deploying the containerized application.
- `README.md`: Project overview and setup instructions.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Docker
- Minikube (or another local Kubernetes solution)
- Ansible
- kubectl
## General Notes:
- ${dockerhub-username}: is your/youe ORG Docker repos.
you may find it in:
```bash
cd ~/Git/AutoDeploymentPipeline/ansible/playbooks/docker_build_push.yaml
cd ~/Git/AutoDeploymentPipeline/ansible/playbooks/k8s_deploy.yaml
cd ~/Git/AutoDeploymentPipeline/k8s/deployment.yaml
```
- Detailed instaltion docmentation for (Docker, )

## General Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/Khalid-Hamad/AutoDeploymentPipeline.git
cd AutoDeploymentPipeline
```

### Step 2: Set Up the Local Kubernetes Cluster
#### 2.1 Start Minikube
```bash
minikube start
```
#### 2.2 Ensure kubectl is configured to use Minikube
```bash
kubectl config use-context minikube
```

### Step 3: Build and Push Docker Image
Navigate to the app/ directory and build the Docker image:
```bash
cd ~/Git/AutoDeploymentPipeline/Docker/app
docker build -t ${dockerhub-username}/myapp:latest .
docker push ${dockerhub-username}/myapp:latest
```
### Step 4: Deploy the Application to Kubernetes
Apply the Kubernetes manifests located in the k8s/ directory:
```bash
cd ~/Git/AutoDeploymentPipeline/k8s
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
### Step 5: Automate with Ansible
Navigate to the ansible/ directory and run the playbooks:
```bash
cd ~/Git/AutoDeploymentPipeline/ansible
```
#### 5.1 Build and push Docker image:
```bash
ansible-playbook playbooks/docker_build_push.yaml
```
#### 5.2 Deploy to Kubernetes:
```bash
ansible-playbook playbooks/k8s_deploy.yaml
```

## Conclusion

This project demonstrates a complete automated deployment pipeline for a containerized web application using Ansible, Docker, and Kubernetes. Follow the setup instructions to recreate the environment on your local machine and explore the provided documentation for a deeper understanding of the architecture and processes involved.
