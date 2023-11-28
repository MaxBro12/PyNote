from core import (
    create_log,

    write_toml,
    read_toml,
    toml_type_check,

    wayfinder,
    create_folder,
)
from sql import create_base

from settings import (
    DIR_DATA,
    DIR_NOTES,
    FILE_SETTINGS,
    FILE_SETTINGS_IN,
    FILE_DB,
)


def main_check() -> dict:
    # ? Проверяем папки
    check_fold(DIR_DATA)
    check_fold(DIR_NOTES)
    # check_db()

    # ? Проверяем файл конфига
    conf = check_conf()

    # ? Проверяем базу пользователей
    check_db()

    return conf


def check_fold(fold: str):
    if not wayfinder(fold):
        create_folder(fold)


def create_settings() -> bool:
    write_toml(FILE_SETTINGS_IN, FILE_SETTINGS)
    create_log(f'FILE {FILE_SETTINGS} CREATED!', 'info')
    return True


def check_conf():
    if not wayfinder(FILE_SETTINGS):
        create_settings()
    else:
        if not toml_type_check(FILE_SETTINGS_IN, read_toml(FILE_SETTINGS)):
            create_settings()
            create_log(f'FILE {FILE_SETTINGS} OVERWRITTEN!', 'error')
    return read_toml(FILE_SETTINGS)


def check_db():
    if not wayfinder(FILE_DB):
        create_base()
        create_log(f'DB {FILE_DB} CREATED!', 'info')
