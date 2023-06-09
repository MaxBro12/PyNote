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

    fold_themes,
    file_dark,
    file_dark_inner,
    file_light,
    file_light_inner,
    file_space,
    file_space_inner,
)
from spec_types import (
    Config,
    cast
)


def main_check() -> Config:
    # ? Проверяем папку с данными
    check_data()
    # ? Проверяем файл конфига
    conf = check_conf()
    # ? Проверяем папку с заметками
    check_notes()
    # ? Проверяем папку с темами
    check_themes()

    return conf


def check_conf() -> Config:
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
    data = read(file_conf)
    config = cast(Config, data)
    # config: Config = {
    #     'app': {
    #         'width': data['app']['width'],
    #         'height': data['app']['height'],
    #         'lang': data['app']['lang'],
    #         'theme': data['app']['theme'],
    #         'opacity': data['app']['opacity'],
    #     },
    #     'user': {
    #         'username': data['user']['username'],
    #         'password': data['user']['password'],
    #         'wtkey': data['user']['wtkey'],
    #     },
    #     'server': {
    #         'host': data['server']['host'],
    #         'token': data['server']['token'],
    #     }
    # }

    return config


def check_notes():
    if not exists(fold_notes):
        mkdir(fold_notes)
        create_log_file('Notes folder created', 'info')


def check_data():
    if not exists(fold_data):
        mkdir(fold_data)
        create_log_file('Data folder created', 'info')


def check_themes():
    if not exists(fold_themes):
        mkdir(fold_themes)
        create_log_file('Themes folder created', 'info')

    if not exists(file_dark):
        write(file_dark_inner, file_dark)
    if not exists(file_light):
        write(file_light_inner, file_light)
    if not exists(file_space):
        write(file_space_inner, file_space)
