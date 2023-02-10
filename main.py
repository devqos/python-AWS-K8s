from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/files")
async def uploadFile(file: UploadFile):
    return {"filename": file.filename}