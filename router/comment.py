from fastapi import APIRouter, status, Response, Path, Query, Body

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


@router.post('/create', summary='Create')
def create_comment(
        id: int = Path(
            title='id',
            description='Post id'
        ),
        comment: str = Body(...)
):
    return {
        'message': f'Comment created on post {id}',
        'data': comment
    }
