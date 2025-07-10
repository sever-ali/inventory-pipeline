# 📦 Inventory App — README

## 📌 Project Overview

A simple MVP Flask-based inventory management concept for stores to track stock, warehousing, and supply chain movements more easily.  
This project demonstrates practical use of Infrastructure as Code (IaC) with Terraform, configuration management with Ansible, containerisation with Docker, and monitoring with Prometheus + Grafana — all deployed to AWS EKS with GitHub Actions CI/CD.

---

## ⚙️ What This Project Uses

- **Terraform** — to provision the underlying AWS infrastructure (VPC, EKS Cluster, IAM Roles, etc.)
- **Ansible** — to configure and deploy the Flask application.
- **Docker** — to containerise the Flask app.
- **Prometheus & Grafana** — to monitor the application.
- **GitHub Actions** — for CI/CD deployment pipeline.

---

## 🗂️ Project Structure

```
inventory-pipeline/
├── terraform-eks/           # Terraform configuration for EKS cluster
│   ├── main.tf
│   └── .terraform.lock.hcl
├── ansible/                 # Ansible playbook and inventory
│   ├── inventory.ini
│   └── playbook.yml
├── inventory_tracker/       # Flask app source code
├── monitoring/              # Prometheus & Grafana config
│   ├── docker-compose.yml
│   └── prometheus.yml
├── .github/workflows/       # CI/CD pipeline workflows
│   ├── deploy.yml
│   └── docker.yml
├── Dockerfile               # Container definition for Flask app
├── docker-compose.yml       # Local Docker Compose (if needed)
├── deployment.yaml          # K8s deployment manifest
├── service.yaml             # K8s service manifest
├── requirements.txt         # Python dependencies
├── .gitignore
├── .dockerignore
└── README.md

---

## 🚀 How To Deploy & Test

### 1️⃣ Provision Infrastructure

1. Install [Terraform](https://developer.hashicorp.com/terraform/install) and configure your AWS credentials.
2. Initialise and apply:
   ```bash
   terraform init
   terraform apply
3.	This will provision your EKS cluster, IAM roles, VPC, subnets, and nodes.

### 2️⃣ Configure & Deploy with Ansible
1.	Install Ansible.
2.	Update ansible/inventory.ini with your EC2 host or bastion IP details.
3.	Run the playbook:
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml

###🐳 3️⃣ Build & Push Docker Image
1.	Build the Docker image locally: docker build -t flask-inventory-app .
2.	Tag & push the image to your container registry (e.g., AWS ECR):
docker tag flask-inventory-app <your-aws-account-id>.dkr.ecr.<region>.amazonaws.com/flask-inventory-app:latest
docker push <your-aws-account-id>.dkr.ecr.<region>.amazonaws.com/flask-inventory-app:latest


###⚡ 4️⃣ CI/CD Pipeline
•	The .github/workflows/ directory includes:
    •	docker.yml to build and push Docker images.
    •	deploy.yml to run Ansible playbooks and configure EC2.
•	Pushing to main will automatically run these workflows.

###🖥️ 5️⃣ Monitoring
•	The monitoring/ folder includes:
	•	docker-compose.yml for Prometheus and Grafana.
	•	prometheus.yml to scrape Flask app metrics.
•	Use docker-compose locally or deploy to your cluster to monitor container metrics.

###✅ Verify
•	Visit http://<your-eks-lb-endpoint> to confirm the Inventory App is running.
•	Access Grafana dashboards to visualise app and container metrics.


###🔒 Notes
Never commit sensitive files (e.g., .pem keys) to a public repo.
Update your security groups to allow HTTP/HTTPS traffic to your instances.
This is an MVP for demonstration; production should secure secrets, keys, and environment variables properly.

This project shows how you can combine Terraform, Ansible, Docker, and Kubernetes on AWS EKS for a simple, repeatable deployment process.