terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.24.0"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.1.0"

  name = "inventory-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-2a", "eu-west-2b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.21.0"

  cluster_name    = "inventory-eks"
  cluster_version = "1.29"

  subnet_ids = module.vpc.private_subnets
  vpc_id     = module.vpc.vpc_id

  enable_irsa = true

  eks_managed_node_groups = {
    default = {
      instance_types = ["t3.medium"]
      min_size       = 1
      max_size       = 1
      desired_size   = 1
    }
  }

  tags = {
    Project = "Project2"
    "terraform-aws-modules" = "eks"
  }
}

