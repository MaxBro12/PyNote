import aiosqlite
from random import randint

from core import load_file, pjoin

from settings import (
    DIR_NOTES,
    FILE_DB,
    MAX_ID_LEN,
    MIN_ID_LEN,
    TABLE_GET_IDS,
    TABLE_GET_USERNAMES
)
from .specclasses import UserData, NoteData


async def db_add_user(data: UserData):
    async with aiosqlite.connect(FILE_DB) as db:
        await db.execute(
            f"""INSERT INTO users (id, username, password)
                VALUES ('{data.id}',
                '{data.username}',
                '{data.password}');"""
        )
        await db.commit()


async def db_remove_user(uid: int):
    async with aiosqlite.connect(FILE_DB) as db:
        await db.execute(
            f"DELETE FROM users WHERE id = '{uid}'"
        )
        await db.commit()


async def db_get_user(username: str):
    async with aiosqlite.connect(FILE_DB) as db:
        async with db.execute(f"SELECT * FROM users WHERE username = '{username}'") as cursor:
            async for row in cursor:
                return UserData(row[0], row[1], row[2])


async def db_add_note(data: NoteData):
    async with aiosqlite.connect(FILE_DB) as db:
        await db.execute(
            f"""INSERT INTO notes (id, notename)
                VALUES ('{data.id}',
                '{data.name}');"""
        )
        await db.commit()


async def db_remove_note(data: NoteData):
    async with aiosqlite.connect(FILE_DB) as db:
        await db.execute(
            f"DELETE FROM notes WHERE id = '{data.id}' AND notename = '{data.name}'"
        )
        await db.commit()


async def db_get_all_user_notes(uid):
    async with aiosqlite.connect(FILE_DB) as db:
        async with db.execute(f"SELECT * FROM notes WHERE id = '{uid}'") as cursor:
            notes = []
            async for row in cursor:
                notes.append(NoteData(row[0], row[1], load_file(pjoin(DIR_NOTES, str(row[0]), row[1]))))
            return notes


async def db_get_ids() -> list:
    async with aiosqlite.connect(FILE_DB) as db:
        cursor = await db.execute(TABLE_GET_IDS)
        ans = []
        async for row in cursor:
            ans.append(row[0])
        return ans


async def db_get_usernames() -> list:
    async with aiosqlite.connect(FILE_DB) as db:
        cursor = await db.execute(TABLE_GET_USERNAMES)
        ans = []
        async for row in cursor:
            ans.append(row[0])
        return ans


async def db_create_id() -> int:
    while True:
        a = randint(MIN_ID_LEN, MAX_ID_LEN)
        if a in await db_get_ids():
            continue
        return a

