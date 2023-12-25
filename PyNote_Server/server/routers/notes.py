from fastapi import APIRouter

from sql import (
    UserData,
    NoteData,
    db_add_note,
    db_remove_note,
    db_get_all_user_notes,
    db_get_notesnames
)
from core import (
    create_note,
    delete_note,
    create_log
)
from .services import check_access


router = APIRouter()


@router.get('/notes')
async def server_get_all_user_notes(token: str, username: str, password: str):
    user = await check_access(token, username, password)
    if type(user) == UserData:
        create_log(f'Get user notes {username}', 'debug')
        return await db_get_all_user_notes(user.id)
    else:
        return user


@router.post('/notes')
async def server_add_note(token: str, username: str, password: str, note: str, inner: str):
    user = await check_access(token, username, password)
    if type(user) == UserData:
        if note not in await db_get_notesnames(user.id):
            await db_add_note(NoteData(user.id, note, ''))
        create_note(user.id, note, inner)
        return {'msg': f'Note {note} CREATED'}
    else:
        return user


@router.delete('/notes')
async def server_delete_note(token: str, username: str, password: str, note: str):
    user = await check_access(token, username, password)
    if type(user) == UserData:
        await db_remove_note(NoteData(user.id, note, ''))
        delete_note(user.id, note)
        return {'msg': f'Note {note} DELETED'}
    else:
        return user
