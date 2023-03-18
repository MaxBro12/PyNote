from os.path import exists
from os import mkdir

from core import write, read, create_log_file

from settings import (
    file_conf,
    file_conf_inner,

    fold_notes,
)


def main_check() -> dict:
    # ? Проверяем файл конфига
    conf = check_conf()
    # ? Проверяем папку с заметками
    check_notes()

    return conf


def check_conf() -> dict:
    if not exists(file_conf):
        write(file_conf_inner, file_conf)
    create_log_file('Config file created', 'info')
    return read(file_conf)


def check_notes():
    if not exists(fold_notes):
        mkdir(fold_notes)
    create_log_file('Notes folder created', 'info')
