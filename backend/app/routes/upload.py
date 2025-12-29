from fastapi import APIRouter, UploadFile, File
from app.services.bg_remove import remove_background
import shutil
import uuid
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    input_path = f"{UPLOAD_DIR}/{file_id}.png"
    output_path = f"{OUTPUT_DIR}/{file_id}_cutout.png"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    remove_background(input_path, output_path)

    return {
        "message": "Background removed successfully",
        "output_image": output_path
    }
from fastapi import APIRouter, UploadFile, File
from app.services.bg_remove import remove_background
import shutil
import uuid
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]

    input_path = f"{UPLOAD_DIR}/{file_id}{ext}"
    output_path = f"{OUTPUT_DIR}/{file_id}_cutout.png"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    remove_background(input_path, output_path)

    return {
        "message": "Background removed successfully",
        "output_image": output_path
    }
