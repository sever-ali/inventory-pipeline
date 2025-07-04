
# 📦 Flask Inventory App on EKS

This project deploys a simple Flask app to an AWS EKS cluster using Terraform and Docker.
It’s set up for learning and testing — pull it, tweak it, break it, fix it!

## 🚀 Tech Stack

- **Flask** — Python web app
- **Docker** — Containerised app image
- **AWS ECR** — Stores the Docker image
- **Terraform** — Manages EKS cluster and node groups
- **Kubernetes** — Deploys the app to EKS

## ✅ Prerequisites

Before you clone and run this, make sure you have:

- AWS account with CLI configured (`aws configure`)
- IAM user with enough permissions (EKS, ECR, EC2, VPC)
- `kubectl` installed and configured
- `terraform` installed
- `docker` installed and running

## 📂 Project Structure

```
.
├── main.tf          # Terraform config for EKS
├── Dockerfile       # Flask app container spec
├── deploy.yaml      # Kubernetes Deployment manifest
├── service.yaml     # Kubernetes Service manifest
├── app/             # Your Flask app code
├── README.md
```

## 🔧 How to Run It Yourself

### 1️⃣ Clone this repo

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Provision the EKS Cluster

```bash
terraform init
terraform apply
```

This spins up your VPC, subnets, EKS cluster and node groups. Wait for it to finish — it may take a few minutes.

### 3️⃣ Build & Push Docker Image to ECR

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.eu-west-2.amazonaws.com

# Build your image
docker build -t flask-inventory-app .

# Tag it
docker tag flask-inventory-app:latest <your-account-id>.dkr.ecr.eu-west-2.amazonaws.com/flask-inventory-app:latest

# Push it
docker push <your-account-id>.dkr.ecr.eu-west-2.amazonaws.com/flask-inventory-app:latest
```

### 4️⃣ Deploy to EKS

```bash
# Update kubeconfig
aws eks --region eu-west-2 update-kubeconfig --name your-cluster-name

# Deploy app and service
kubectl apply -f deploy.yaml
kubectl apply -f service.yaml

# Check pods
kubectl get pods
kubectl get svc
```

### 5️⃣ Access the App

Look for the `EXTERNAL-IP` of the LoadBalancer:

```bash
kubectl get svc
```

Open it in your browser and you should see your Flask app running on EKS!

## 🗑️ Cleanup

To avoid unwanted AWS charges:

```bash
terraform destroy
```

## 📝 License

MIT — do what you want with it.

**Happy building!** 🚢✨
