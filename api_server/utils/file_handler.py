import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

def ensure_upload_dir():

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)


async def save_uploaded_file(file: UploadFile):

    ensure_upload_dir()

    ext = file.filename.split(".")[-1]

    filename = f"{uuid.uuid4()}.{ext}"

    file_path = os.path.join(UPLOAD_DIR, filename)

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    return file_path