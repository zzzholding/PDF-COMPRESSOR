from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os 

app = FastAPI()
uploads = "uploads" # os.makedirs(uploads, exist_ok=True)

@app.get("/")
def root():
    return{"message":"Server connect"}

@app.post("/process/")
async def proc(file:UploadFile = File()):
    input_path = os.path.join(uploads, file.filename) # получаем
    with open(input_path, "wb") as buffer: # я буду записывать байт откроем 
        buffer.write(await file.read()) # читаем записываем сохр в buffer и закрываем

        return FileResponse( 
            path = input_path, #конкретный стандарт path параметр 
            media_type='application/pdf', #чтобы браузер понял что 
            filename="compressed_" + file.filename  
        )
        
        


