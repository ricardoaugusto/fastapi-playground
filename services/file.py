import shutil

from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/file", tags=["file"])


def upload_file(upload_content: UploadFile = File(...)):
    path = f"files/{upload_content.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(upload_content.file, buffer)

    return {"filename": path, "type": upload_content.content_type}


def download_file(name: str):
    path = f"files/{name}"
    return path
