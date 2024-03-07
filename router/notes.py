from enum import Enum
from typing import Optional

from fastapi import APIRouter, status, Response, Query, Path, Body

from schemas.note import Note as NoteModel

router = APIRouter(prefix="/note", tags=["note"])


"""
FastAPI no-db concepts practice with Note
"""


class NoteType(Enum):
    short = "short"
    long = "long"
    task = "task"


@router.get("/")
def page(
    page: int = Query(1, title="page", description="Page number"),
    per_page: Optional[int] = Query(
        10, title="per_page", description="How many notes per page"
    ),
):
    return {
        "message": f"all {per_page} notes on page {page}",
        "page": page,
        "per_page": per_page,
    }


@router.get("/type/{type}")
def note(type: NoteType):
    return {"message": f"Note type: {type.name}"}


@router.get("/{id}")
def note(id: int = Path(..., gt=5, le=10), response: Response = Response()):
    """
    If the id is greater than 9, return HTTP 404
    """
    if id > 9:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Note id not found"}
    else:
        return {"message": "Note id: {}".format(id)}


@router.post("/create")
def create_note(
    note: NoteModel = Body(
        None, title="note", description="NoteModel", user_id="integer"
    )
):
    return {"message": "Note created", "data": note}


@router.patch("/{id}/update")
def update_note(
    note: NoteModel = Body(None, title="note", description="NoteModel"),
    id: int = Path(title="id", description="Id of the note"),
):
    return {"id": id, "message": "Note updated", "data": note}
