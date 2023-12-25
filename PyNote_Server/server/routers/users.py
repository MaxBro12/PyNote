from fastapi import APIRouter
from sql import UserData, db_add_user, db_remove_user, db_get_usernames, db_create_id
from core import create_log, delete_userfolder

from .services import correct_token, check_access


router = APIRouter()


@router.post('/user')
async def server_new_user(token: str, username: str, password: str):
    if correct_token(token):
        if username in await db_get_usernames():
            return {'msg': 'exist'}
        else:
            uid = await db_create_id()
            await db_add_user(UserData(uid, username, password))
            create_log(f'Added user {username}', 'debug')
            return {'msg': 'All good'}
    return {'msg': 'Wrong token'}


@router.delete('/user')
async def server_delete_user(token: str, username: str, password: str):
    user = await check_access(token, username, password)
    if type(user) == UserData:
        await db_remove_user(user.id)
        delete_userfolder(user.id)
        create_log(f'Deleted user {username}', 'debug')
        return {'msg': f'User {username} DELETED'}
    else:
        return user
