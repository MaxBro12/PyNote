from typing import Final


# ! Основное
DIR_DATA: Final = 'server_data'

FILE_SETTINGS: Final = f'{DIR_DATA}/settings.toml'
FILE_SETTINGS_IN: Final = {
    'SERVER': {
        'HOST': "",
        'PORT': 8000,
        'TOKEN': "",
        'DEBUG': "",
    },
}

FILE_LOGGER = f'{DIR_DATA}/logger.log'
FILE_ERROR = f'{DIR_DATA}/error.log'

FILE_DB = f'{DIR_DATA}/base.sqlite3'

DIR_NOTES = f'{DIR_DATA}/notes'


# ! SQL
MAX_ID_LEN: Final = 1_000_000
MIN_ID_LEN: Final = 100_010

CREATE_TABLE_USERS: Final = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL);"""
CREATE_TABLE_NOTES: Final = """CREATE TABLE IF NOT EXISTS notes (
        id INTEGER NOT NULL,
        notename TEXT NOT NULL,
        CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES users(id)
    );"""

TABLE_GET_IDS: Final = """SELECT id FROM users"""
TABLE_GET_USERNAMES: Final = """SELECT username FROM users"""

