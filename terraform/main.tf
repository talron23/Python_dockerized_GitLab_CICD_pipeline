terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.21.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

module "ecs_fargate" {
  source = "./ecs"
  image_uri = "talron23/joke:python-app-2.0"
}
