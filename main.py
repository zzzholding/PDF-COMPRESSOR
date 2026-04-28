from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os 

app = FastAPI()
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def root():
    return{"message":"Server connect"}

@app.post("/process/")
async def proc(file:UploadFile = File()):
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())
        return FileResponse(
            path = input_path,
            media_type='application/octet-stream',
            filename=file.filename
        )


