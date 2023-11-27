from fastapi import APIRouter


router = APIRouter()
db = -

@router.get('/user')
def new_user(token: str, username: str, password: str):
    if config['token'] == token:
        if username in db.users:
            return {'msg': 'exist'}
        else:
            db.add({})
