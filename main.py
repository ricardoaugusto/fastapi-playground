from fastapi import FastAPI
from router import post, comment

app = FastAPI()

app.include_router(post.router)
app.include_router(comment.router)


@app.get('/')
def index():
    return {"message": "Hello World"}
