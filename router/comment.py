from fastapi import APIRouter, status, Response

router = APIRouter(
    prefix='/posts/{id}/comments',
    tags=['comments']
)


@router.get('', summary='Get {n} comments from a post {id}', description='Query string {n}')
def comments(id: int, n: int = 10):
    return {"message": f'Post id: {id} comments: {n}'}
