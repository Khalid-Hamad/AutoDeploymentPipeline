# Ansible Playbooks

This directory contains Ansible playbooks for automating the Docker image build/push process and the deployment of the application to a Kubernetes cluster.
## Ansible installtion 

- offical Ansible [installation guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html).
- Ansible check installation command: 
   ```bash
   ansible --version
   ```


## Prerequisites

- Ansible installed on your local machine.
- Docker installed and running.
- Minikube or another local Kubernetes solution installed and running.
- kubectl configured to interact with your local Kubernetes cluster.

## Directory Structure
   ```bash
ansible/
├── playbooks/
│   ├── docker_build_push.yaml
│   └── k8s_deploy.yaml
└── README.md
```
## Playbooks

### 1. docker_build_push.yaml

This playbook automates the process of building a Docker image for the sample web application and pushing it to a Docker registry.
### 2. k8s_deploy.yaml
This playbook automates the deployment of the sample web application to a Kubernetes cluster using the provided Kubernetes manifests.
#### Usage

1. Navigate to the `ansible/` directory:
   ```bash
   cd ~/Git/AutoDeploymentPipeline/ansible
   ```
2. Command Line explan:
   ```bash
   ansible-playbook playbooks/${file_name}.yaml
   ```
   