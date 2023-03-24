from os.path import exists
from os import mkdir

from core import write, read, create_log_file

from settings import (
    fold_data,

    file_conf,
    file_conf_inner,

    fold_notes,
)


def main_check() -> dict:
    # ? Проверяем папки
    check_fold(fold_data)
    check_fold(fold_notes)

    # ? Проверяем файл конфига
    conf = check_conf()

    # ? Проверяем базу пользователей
    check_db()

    return conf


def check_fold(fold: str):
    if not exists(fold):
        mkdir(fold)
    create_log_file(f'{fold} folder created', 'info')


def check_conf() -> dict:
    if not exists(file_conf):
        write(file_conf_inner, file_conf)
    create_log_file('Config file created', 'info')
    return read(file_conf)


def check_db():
    pass
