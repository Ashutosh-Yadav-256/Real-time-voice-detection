terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "voice-detect-tfstate"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "voice-detect-tflock"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = local.common_tags
  }
}

locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

module "vpc" {
  source             = "../../modules/vpc"
  environment        = var.environment
  project            = var.project
  vpc_cidr           = var.vpc_cidr
  availability_zones = var.availability_zones
  private_subnets    = var.private_subnets
  public_subnets     = var.public_subnets
  enable_nat_gateway = true
  single_nat_gateway = false
  tags               = local.common_tags
}

module "eks" {
  source          = "../../modules/eks"
  cluster_name    = "${var.project}-${var.environment}"
  cluster_version = var.cluster_version
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids
  environment     = var.environment
  tags            = local.common_tags
}

module "ecr" {
  source      = "../../modules/ecr"
  project     = var.project
  environment = var.environment
  repositories = [
    "ingestion",
    "preprocessor",
    "feature-extractor",
    "inference-router",
    "event-consumer",
    "api-gateway"
  ]
  tags = local.common_tags
}

module "msk" {
  source              = "../../modules/msk"
  cluster_name        = "${var.project}-${var.environment}"
  kafka_version       = "3.5.1"
  broker_count        = 3
  broker_instance_type = "kafka.m5.xlarge"
  subnet_ids          = module.vpc.private_subnet_ids
  vpc_id              = module.vpc.vpc_id
  ebs_volume_size     = 500
  kms_key_arn         = module.kms.key_arn
  tags                = local.common_tags
}

module "rds" {
  source            = "../../modules/rds"
  identifier        = "${var.project}-${var.environment}"
  engine_version    = "15.4"
  instance_class    = "db.r6g.large"
  allocated_storage = 200
  db_name           = "voice_metadata"
  subnet_ids        = module.vpc.private_subnet_ids
  vpc_id            = module.vpc.vpc_id
  kms_key_arn       = module.kms.key_arn
  multi_az          = true
  tags              = local.common_tags
}

module "elasticache" {
  source         = "../../modules/elasticache"
  cluster_name   = "${var.project}-${var.environment}"
  node_type      = "cache.r6g.large"
  num_cache_nodes = 3
  subnet_ids     = module.vpc.private_subnet_ids
  vpc_id         = module.vpc.vpc_id
  tags           = local.common_tags
}

module "kms" {
  source      = "../../modules/kms"
  project     = var.project
  environment = var.environment
  tags        = local.common_tags
}

module "s3" {
  source      = "../../modules/s3"
  project     = var.project
  environment = var.environment
  kms_key_arn = module.kms.key_arn
  tags        = local.common_tags
}
