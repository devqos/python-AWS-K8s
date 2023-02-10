import boto3
import config
from botocore.config import Config

def generatePresignedUrl(bucket, object, expiration):
    client = boto3.client('s3', use_ssl=False, aws_access_key_id=config.AWS_ACCESS_KEY_ID, aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY, region_name=config.REGION_NAME, config=Config(signature_version='s3v4'))
    response = client.generate_presigned_post(bucket, object, ExpiresIn = expiration)

    return response