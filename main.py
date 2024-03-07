from fastapi import FastAPI, Query
from router import post, user
from db.database import engine
from db import models

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

models.Base.metadata.create_all(bind=engine)


@app.get('/')
def index(
        version: int = Query(
            1,
            description='Revision version',
            alias='v',
            deprecated=True
        )
):
    return {"message": "Hello World"}
