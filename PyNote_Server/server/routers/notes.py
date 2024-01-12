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
from .server_models import UserModel, CreateNoteModel, DeleteNoteModel


router = APIRouter()


@router.get('/notes')
async def server_get_all_user_notes(usermodel: UserModel):
    user = await check_access(
        usermodel.token,
        usermodel.username,
        usermodel.password
    )
    if type(user) == UserData:
        create_log(f'Get user notes {user.id}', 'debug')
        return await db_get_all_user_notes(user.id)
    else:
        return user


@router.post('/notes')
async def server_add_note(notemodel: CreateNoteModel):
    user = await check_access(
        notemodel.token,
        notemodel.username,
        notemodel.password
    )
    if type(user) == UserData:
        if notemodel.note not in await db_get_notesnames(user.id):
            await db_add_note(NoteData(user.id, notemodel.note, ''))
        create_note(user.id, notemodel.note, notemodel.inner)
        return {'msg': f'Note {notemodel.note} CREATED'}
    else:
        return user


@router.delete('/notes')
async def server_delete_note(notemodel: CreateNoteModel):
    user = await check_access(
        notemodel.token,
        notemodel.username,
        notemodel.password
    )
    if type(user) == UserData:
        await db_remove_note(NoteData(user.id, notemodel.note, ''))
        delete_note(user.id, notemodel.note)
        return {'msg': f'Note {notemodel.note} DELETED'}
    else:
        return user
