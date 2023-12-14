import sqlite3

from core import create_log

from settings import (
    CREATE_TABLE_USERS,
    CREATE_TABLE_NOTES,
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
