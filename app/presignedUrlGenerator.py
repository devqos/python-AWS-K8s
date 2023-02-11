import boto3
import app.config as config

def generatePresignedUrl(bucket, object, expiration):
    client = boto3.client('s3')

    response = client.generate_presigned_post(bucket, object, ExpiresIn = expiration)

    return response