from fastapi import FastAPI, status, Response
from PostType import *

app = FastAPI()


@app.get('/')
def index():
    return {"message": "Hello World"}


@app.get('/posts', tags=['post'])
def page(page: int = 1, per_page: int = 10):
    return {"message": f'all {per_page} posts on page {page}', "page": page, "per_page": per_page}


@app.get('/posts/type/{type}', tags=['post'])
def post(type: PostType):
    return {"message": f'Post type: {type.name}'}


@app.get('/posts/{id}', tags=['post'])
def post(id: int, response: Response = Response()):
    """
    If the id is greater than 5, return HTTP 404
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Post id not found"}
    else:
        return {"message": "Post id: {}".format(id)}


@app.get('/posts/{id}/comments', tags=['comments'], summary='Get {n} comments from a post', description='Query string {comments}')
def comments(id: int, comments: int = 10):
    return {"message": f'Post id: {id} comments: {comments}'}
