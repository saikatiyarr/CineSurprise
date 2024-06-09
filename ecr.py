import boto3

ecr_client = boto3.client('ecr')

repository_name = "my-first-app-repo"
responce = ecr_client.create_repository()
