import sqlite3
from random import randint

from core import create_log, update_dict_to_type

from settings import (
    FILE_DB,

    CREATE_TABLE_USERS,
    CREATE_TABLE_NOTES,

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

    def update(self):
        self.data.commit()

    def add_user(self, data: UserData):
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

    def add_note(self, data: NoteData):
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

    def remove_user(self, uid: int) -> list | None:
        if self.find(uid):
            a = self.cursor.execute(
                f"DELETE FROM users WHERE id = '{uid}'"
            ).fetchall()
            self.data.commit()
            create_log(f'User {uid} was deleted', 'info')
            return a
        else:
            create_log(f'Unable delete ID {uid}')
            return None

    def remove_note(self, data: NoteData) -> list | None:
        if self.find(data.id):
            a = self.cursor.execute(
                f"DELETE FROM note WHERE id = '{data.id}' AND notename = '{data.name}'"
            ).fetchall()
            self.data.commit()
            create_log(f'User {data.id} was deleted', 'info')
            return a
        else:
            create_log(f'Unable delete ID {data.id}')
            return None

    def find(self, uid: int) -> bool:
        try:
            return True if self.cursor.execute(
                f"SELECT EXISTS (SELECT 1 FROM users WHERE id = '{uid}');"
            ).fetchall()[0][0] == 1 else False
        except IndexError:
            create_log(f'Cant find user by id {uid}')
            return False

    def create_id(self) -> int:
        while True:
            a = randint(MIN_ID_LEN, MAX_ID_LEN)
            if a in self.ids:
                continue
            return a

    def get_notes(self, uid: int) -> tuple:
        try:
            sql_answer = self.cursor.execute(
                f"SELECT * FROM notes WHERE id = '{uid}'"
            ).fetchall()
            ans = tuple(map(lambda x: NoteData(x[0], x[1]), sql_answer))
            return ans
        except IndexError:
            create_log(f'Cant find user by id {uid}')
            return ()

    def get_user_data(self, username: str) -> UserNoteData | None:
        try:
            a = self.cursor.execute(
                f"SELECT * FROM users WHERE username = '{username}'"
            ).fetchall()
            a = UserData(a[0][0], a[0][1], a[0][2])
            return UserNoteData(a, self.get_notes(a.id))
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


def create_base(db_name: str) -> sqlite3.Connection | None:
    """Создает базу данных"""
    try:
        sql = sqlite3.connect(db_name)
        sqlcursor = sql.cursor()

        sqlcursor.execute(CREATE_TABLE_USERS)
        sql.commit()

        sqlcursor.execute(CREATE_TABLE_NOTES)
        sql.commit()
        sqlcursor.close()

        return sql

    except sqlite3.Error as error:
        create_log(error, 'error')


# def load_db(db_name: str = FILE_DB) -> sqlite3.Connection | None:
#     """Возвращается база данных под названием db_name.
#     Обязательно! Файл должен быть с расширением .db"""
#     return sqlite3.connect(db_name)
