from fastapi import FastAPI, Query
from router import post, comment

app = FastAPI()

app.include_router(post.router)
app.include_router(comment.router)


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
