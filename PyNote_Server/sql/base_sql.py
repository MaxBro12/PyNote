import sqlite3
from random import randint

from core import create_log
from .create_sql import create_base

from settings import (
    FILE_DB,
    TABLE_GET_USERNAMES,
    TABLE_GET_IDS,

    MAX_ID_LEN,
    MIN_ID_LEN,
)
from .specclasses import UserData, NoteData, UserNoteData, Singleton
from .exceptions import LoadDBException


class DataBase(Singleton):
    def __init__(self, db_name: str = FILE_DB):
        data = create_base(db_name)
        if data is not None:
            self.data = data
            self.cursor = self.data.cursor()
        else:
            raise LoadDBException

    async def update(self):
        self.data.commit()

    async def add_user(self, data: UserData):
        try:
            self.cursor.execute(
                f"""INSERT INTO users (id, username, password)
                VALUES ('{data.id}',
                '{data.username}',
                '{data.password}');"""
            )
            self.data.commit()
            create_log(f'User ID {data.id} added', 'info')
        except sqlite3.IntegrityError:
            create_log(f'Cant add ID {data.id}', 'error')

    async def add_note(self, data: NoteData):
        try:
            self.cursor.execute(
                f"""INSERT INTO notes (id, notename)
                VALUES ('{data.id}',
                '{data.name}');"""
            )
            self.data.commit()
            create_log(f'User ID {data.id} added', 'info')
        except sqlite3.IntegrityError:
            create_log(f'Cant add ID {data.id}', 'error')

    async def remove_user(self, uid: int) -> list | None:
        if self.id_in(uid):
            a = self.cursor.execute(
                f"DELETE FROM users WHERE id = '{uid}'"
            ).fetchall()
            self.data.commit()
            create_log(f'User {uid} was deleted', 'info')
            return a
        else:
            create_log(f'Unable delete ID {uid}')
            return None

    async def remove_note(self, data: NoteData) -> list | None:
        if self.id_in(data.id):
            a = self.cursor.execute(
                f"DELETE FROM note WHERE id = '{data.id}' AND notename = '{data.name}'"
            ).fetchall()
            self.data.commit()
            create_log(f'User {data.id} was deleted', 'info')
            return a
        else:
            create_log(f'Unable delete ID {data.id}')
            return None

    async def id_in(self, uid: int) -> bool:
        try:
            return True if self.cursor.execute(
                f"SELECT EXISTS (SELECT 1 FROM users WHERE id = '{uid}');"
            ).fetchall()[0][0] == 1 else False
        except IndexError:
            create_log(f'Cant find user by id {uid}')
            return False

    async def name_in(self, username: str) -> bool:
        try:
            return True if self.cursor.execute(
                f"SELECT EXISTS (SELECT 1 FROM users WHERE username = '{username}');"
            ).fetchall()[0][0] == 1 else False
        except IndexError:
            create_log(f'Cant find user by name {username}')
            return False

    async def create_id(self) -> int:
        while True:
            a = randint(MIN_ID_LEN, MAX_ID_LEN)
            if a in self.ids:
                continue
            return a
    
    async def get_user(self, username: str) -> UserData | None:
        try:
            sql_answer = self.cursor.execute(
                f"SELECT * FROM users WHERE username = '{username}'"
            ).fetchall()
            return UserData(sql_answer[0][0], sql_answer[0][1], sql_answer[0][2])
        except IndexError:
            create_log(f'Cant find user by name {username}')

    async def get_notes(self, uid: int) -> tuple[NoteData, ...]:
        try:
            sql_answer = self.cursor.execute(
                f"SELECT * FROM notes WHERE id = '{uid}'"
            ).fetchall()
            ans = tuple(map(lambda x: NoteData(x[0], x[1]), sql_answer))
            return ans
        except IndexError:
            create_log(f'Cant find user by id {uid}')
            return ()

    async def get_user_data(self, username: str) -> UserNoteData | None:
        try:
            a = self.cursor.execute(
                f"SELECT * FROM users WHERE username = '{username}'"
            ).fetchall()
            a = UserData(a[0][0], a[0][1], a[0][2])
            return UserNoteData(a, await self.get_notes(a.id))
        except IndexError:
            create_log(f'Cant find user by name {username}')

    @property
    def ids(self) -> tuple:
        return tuple(
            map(lambda x: x[0],
                self.cursor.execute(TABLE_GET_IDS).fetchall())
        )

    @property
    def users(self) -> tuple:
        return tuple(
            map(lambda x: x[0],
                self.cursor.execute(TABLE_GET_USERNAMES).fetchall())
        )
