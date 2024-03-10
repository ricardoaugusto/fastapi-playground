import os

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine
from router import authentication, post, user, notes, file

app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(file.router)
app.include_router(notes.router)

files_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "files"
)
app.mount("/files", StaticFiles(directory=files_directory), name="files")

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def index(
    version: int = Query(
        1, description="Revision version", alias="v", deprecated=True
    )
):
    return {"message": "Hello World"}


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
