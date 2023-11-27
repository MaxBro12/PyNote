import sqlite3

from core import create_log, update_dict_to_type

from settings import (
    FILE_DB,

    CREATE_TABLE,
    TABLE_GET_USERNAMES,
)
from .specclasses import UserData


class DataBase:
    def __init__(self, db_name: str = FILE_DB):
        self.data = load_db(db_name)
        self.cursor = self.data.cursor()

    def update(self):
        self.data.commit()

    def add(self, data: dict):
        try:
            self.cursor.execute(
                f"""INSERT INTO users (id, username, password, token)
                VALUES ('{data['id']}',
                '{data['username']}',
                '{data['password']}');"""
            )
            self.data.commit()
            create_log(f'User ID {data["id"]} added', 'info')
        except sqlite3.IntegrityError:
            create_log(f'Cant add ID {data["id"]}', 'error')

    def remove(self, uid: int) -> list | None:
        if self.get(uid) is not None:
            a = self.cursor.execute(
                f"DELETE FROM users WHERE id = '{uid}'"
            ).fetchall()
            self.data.commit()
            create_log(f'User {uid} was deleted', 'info')
            return a
        else:
            create_log(f'Unable delete ID {uid}')
            return None

    def get(self, uid: int) -> UserData | None:
        try:
            a = self.cursor.execute(
                f"SELECT * FROM users WHERE id = '{uid}'"
            ).fetchall()
            return update_dict_to_type({
                'id': a[0][0],
                'username': a[0][1],
                'password': a[0][2],
            }, UserData)
        except IndexError:
            create_log(f'Cant find user by id {uid}')
            return None

    def get_by_name(self, username: str) -> UserData | None:
        try:
            a = self.cursor.execute(
                f"SELECT * FROM users WHERE username = '{username}'"
            ).fetchall()
            return update_dict_to_type({
                'id': a[0][0],
                'username': a[0][1],
                'password': a[0][2],
            }, UserData)
        except IndexError:
            create_log(f'Cant find user by name {username}')
            return None

    @property
    def users(self) -> tuple:
        return tuple(
            map(lambda x: x[0],
                self.cursor.execute(TABLE_GET_USERNAMES).fetchall())
        )

    # @property
    # def id_list(self) -> list:
    #     return list(
    #         map(lambda x: x[0],
    #             self.cursor.execute(CREATE_TABLE_get_id).fetchall())
    #     )


def create_base():
    """Создает базу данных"""
    try:
        sql = sqlite3.connect(FILE_DB)
        sqlcursor = sql.cursor()

        sqlcursor.execute(CREATE_TABLE)
        sql.commit()
        sqlcursor.close()

    except sqlite3.Error as error:
        create_log(error, 'error')


def load_db(db_name: str = FILE_DB) -> sqlite3.Connection:
    """Возвращается база данных под названием db_name.
    Обязательно! Файл должен быть с расширением .db"""
    try:
        return sqlite3.connect(db_name)
    except Exception as error:
        create_log(error, 'error')
        return sqlite3.Connection(CREATE_TABLE)
