from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse

from auth.oauth2 import get_current_user
from schemas.user import UserBase
from services import file as file_service

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/upload")
def get_uploadfile(
    file: UploadFile = File(...),
    current_user: UserBase = Depends(get_current_user),
):
    return file_service.upload_file(file)


@router.get("/download/{name}", response_class=FileResponse)
def get_file(name: str):
    return file_service.download_file(name)
