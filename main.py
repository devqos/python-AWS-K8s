from fastapi import FastAPI, UploadFile
from presignedUrlGenerator import *
import config
import requests

app = FastAPI()

@app.post("/files")
async def uploadFile(file: UploadFile):
    response = generatePresignedUrl(config.BUCKET_NAME, file.filename, 3600)
    files = {"file": file.file}
    s3Response = requests.post(response['url'], data=response['fields'], files=files)
    return s3Response.status_code