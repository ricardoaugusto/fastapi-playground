from fastapi import APIRouter, Path, Query

from schemas import comment

router = APIRouter(
    prefix='/post/{id}/comments',
    tags=['comments']
)


@router.get('',
            summary='Get {n} comments from a post {id}',
            description='Query string {n}')
def comments(
        id: int = Path(
            title='id',
            description='Post id'
        ),
        n: int = Query(
            10,
            description='How many comments to return',
            alias='perPage'
        )
):
    return {"message": f'Post id: {id} comments: {n}'}


@router.post('/create', summary='Create a comment')
def create_comment(
        id: int,
        comment: comment.CreateCommentRequest
):
    return {
        'message': f'Comment created on post {id}',
        'data': comment.comment,
        'version': comment.v
    }
