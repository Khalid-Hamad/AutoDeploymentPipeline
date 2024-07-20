# Kubernetes (k8s)

This directory contains the Kubernetes manifests for deploying the sample web application to a Kubernetes cluster.

## Prerequisites
- Minikube or another local Kubernetes solution installed and running.
- kubectl configured to interact with your local Kubernetes cluster.


## Minikube Inastaltion 
there are many tools for running (Minikube) on local Devolopers machine, personaly I used (Podman Machine) for many usge local Kubernetes and Minikube are one of them: 
- Install [Podman Machine](https://podman.io/docs/installation) Gidelines. 

## Directory Structure
   ```bash
k8s/
├── deployment.yaml
├── service.yaml
└── README.md
```
## Manifests

### deployment.yaml

Defines the Deployment for the sample web application.

### service.yaml

Defines the Service to expose the sample web application via a LoadBalancer.

## Usage

1. Ensure your local Minikube is running.
2. Navigate to the `k8s/` directory:
   ```bash
   cd ~/Git/AutoDeploymentPipeline/k8s
   ```
3. kubectl explean: 
   ```bash
   kubectl apply -f ${file_name}.yaml
   ```
4. Get the URL of the LoadBalancer service:
   ```bash
   minikube service ${app_name} --url
   ```