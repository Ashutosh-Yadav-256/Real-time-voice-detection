aws_region         = "us-east-1"
environment        = "prod"
project            = "voice-detect"
vpc_cidr           = "10.2.0.0/16"
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
private_subnets    = ["10.2.1.0/24", "10.2.2.0/24", "10.2.3.0/24"]
public_subnets     = ["10.2.101.0/24", "10.2.102.0/24", "10.2.103.0/24"]
cluster_version    = "1.28"
