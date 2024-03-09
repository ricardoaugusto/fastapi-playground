from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from db import models
from db.database import engine
from router import authentication, post, user, notes

app = FastAPI()


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(notes.router)

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
