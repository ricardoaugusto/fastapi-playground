from fastapi import APIRouter, status, Response
from typing import Optional
from PostType import *
from models.Post import Post as PostModel

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.get('/')
def page(page: int = 1, per_page: Optional[int] = 10):
    return {"message": f'all {per_page} posts on page {page}', "page": page, "per_page": per_page}


@router.get('/type/{type}')
def post(type: PostType):
    return {"message": f'Post type: {type.name}'}


@router.get('/{id}')
def post(id: int, response: Response = Response()):
    """
    If the id is greater than 5, return HTTP 404
    """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Post id not found"}
    else:
        return {"message": "Post id: {}".format(id)}


@router.post('/create')
def create_post(post: PostModel):
    return {"message": post}
