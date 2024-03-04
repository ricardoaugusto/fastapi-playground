from fastapi import APIRouter, status, Response, Query, Path, Body
from typing import Optional
from router.PostType import *
from schemas.post import Post as PostModel

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.get('/')
def page(
        page: int = Query(
            1,
            title='page',
            description='Page number'
        ),
        per_page: Optional[int] = Query(
            10,
            title='per_page',
            description='How many posts per page'
        )
):
    return {"message": f'all {per_page} posts on page {page}', "page": page, "per_page": per_page}


@router.get('/type/{type}')
def post(type: PostType):
    return {"message": f'Post type: {type.name}'}


@router.get('/{id}')
def post(
        id: int = Path(..., gt=5, le=10),
        response: Response = Response()
):
    """
    If the id is greater than 9, return HTTP 404
    """
    if id > 9:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Post id not found"}
    else:
        return {"message": "Post id: {}".format(id)}


@router.post('/create')
def create_post(
        post: PostModel = Body(
            None,
            title='post',
            description='PostModel'
        )
):
    return {
        "message": 'Post created',
        'data': post
    }


@router.patch('/{id}/update')
def update_post(
        post: PostModel = Body(
            None,
            title='post',
            description='PostModel'
        ),
        id: int = Path(
            title='id',
            description='Id of the post'
        )
):
    return {
        'id': id,
        "message": 'Post updated',
        'data': post
    }
