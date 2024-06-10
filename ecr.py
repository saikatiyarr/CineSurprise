import boto3
from botocore.exceptions import ClientError

client = boto3.client('ecr')

repo_name = "movie-app-repo"

try:
    response = client.create_repository(repositoryName=repo_name)
    repo_uri = response['repository']['repositoryUri']
    print(f"Repository URI: {repo_uri}")
except ClientError as e:
    print(f"Error: {e.response['Error']['Message']}")
