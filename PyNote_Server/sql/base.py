import sqlite3

from settings import (
    file_db,
    table,

    table_get_id,
    table_get_users,
)
from core import create_log_file


class DataBase:
    def __init__(self, db_name: str = file_db):
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
                '{data['password']}',
                '{data['token']}');"""
            )
            self.data.commit()
            create_log_file(f'User ID {data["id"]} added', 'info')
        except sqlite3.IntegrityError:
            create_log_file(f'Cant add ID {data["id"]}', 'error')

    def remove(self, uid: int) -> list | None:
        if self.get(uid) is not None:
            a = self.cursor.execute(
                f"DELETE FROM users WHERE id = '{uid}'"
            ).fetchall()
            self.data.commit()
            create_log_file(f'User {uid} was deleted', 'info')
            return a
        else:
            create_log_file(f'Unable delete ID {uid}')
            return None

    def get(self, uid: int) -> dict | None:
        try:
            a = self.cursor.execute(
                f"SELECT * FROM users WHERE id = '{uid}'"
            ).fetchall()
            return {
                'id': a[0][0],
                'username': a[0][1],
                'password': a[0][2],
                'token': a[0][3],
            }
        except IndexError:
            create_log_file(f'Cant find user by id {uid}')
            return None

    def get_by_name(self, username: str) -> dict | None:
        try:
            a = self.cursor.execute(
                f"SELECT * FROM users WHERE username = '{username}'"
            ).fetchall()
            return {
                'id': a[0][0],
                'username': a[0][1],
                'password': a[0][2],
                'token': a[0][3],
            }
        except IndexError:
            create_log_file(f'Cant find user by name {username}')
            return None

    @property
    def user_list(self) -> list:
        return list(
            map(lambda x: x[0],
                self.cursor.execute(table_get_users).fetchall())
        )

    @property
    def id_list(self) -> list:
        return list(
            map(lambda x: x[0],
                self.cursor.execute(table_get_id).fetchall())
        )


def create_base():
    """Создает базу данных"""
    try:
        sql = sqlite3.connect(file_db)
        sqlcursor = sql.cursor()

        sqlcursor.execute(table)
        sql.commit()
        sqlcursor.close()

    except sqlite3.Error as error:
        create_log_file(error, 'error')


def load_db(db_name: str = file_db) -> sqlite3.Connection:
    """Возвращается база данных под названием db_name.
    Обязательно! Файл должен быть с расширением .db"""
    try:
        return sqlite3.connect(db_name)
    except Exception as error:
        create_log_file(error, 'error')
        return sqlite3.Connection(table)
