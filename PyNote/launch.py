from os.path import exists
from os import mkdir

from re import fullmatch

from core import write, read, create_log_file

from settings import (
    fold_data,
    file_conf,
    file_conf_inner,
    file_conf_row,

    fold_notes,
)


def main_check() -> dict:
    # ? Проверяем папку с данными
    check_data()
    # ? Проверяем файл конфига
    conf = check_conf()
    # ? Проверяем папку с заметками
    check_notes()

    return conf


def check_conf() -> dict:
    if not exists(file_conf):
        write(file_conf_inner, file_conf)
        create_log_file('Config file created', 'info')
    with open(file_conf, 'r') as fle:
        text = fle.readlines()
        text = ''.join(text)
        if not fullmatch(file_conf_row, text):
            write(file_conf_inner, file_conf)
            create_log_file(
                f'Error in {file_conf}, file has been overwritten!', 'error'
            )
    return read(file_conf)


def check_notes():
    if not exists(fold_notes):
        mkdir(fold_notes)
        create_log_file('Notes folder created', 'info')


def check_data():
    if not exists(fold_data):
        mkdir(fold_data)
        create_log_file('Data folder created', 'info')
