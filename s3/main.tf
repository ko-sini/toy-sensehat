terraform {
  required_version = ">=1.0.10"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.62.0"
    }
  }

  backend "s3" {
    bucket = "master-eu-north-1-remote-state"
    key    = "raspi/raspi-eu-north-1-remote-state.tfstate"
    region = "eu-north-1"
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "eu-north-1"
}

# Create S3
resource "aws_s3_bucket" "remote_state" {
  bucket_prefix = "raspi-${var.region}-storage"
}