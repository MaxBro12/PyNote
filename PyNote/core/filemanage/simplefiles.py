from ..debug import create_log_file

from os import rename, listdir


def create_file(
    name: str,
    inner_text: str = ''
) -> bool:
    try:
        # ! Создание
        with open(name, 'w') as f:
            if inner_text != '':
                f.write(inner_text)
            f.close()
        return True
    except FileExistsError:
        create_log_file(f'Файл {name} уже существует!', 'error')
        return False
    except FileNotFoundError:
        create_log_file(f'Файл {name} не существует', 'error')
        return False


def load_file(name: str) -> str:
    try:
        with open(name, 'r') as f:
            return ''.join(f.readlines())
    except FileNotFoundError:
        create_log_file(f'Файл {name} не найден')
        return ''


def rename_file(last_name: str, new_name: str):
    try:
        rename(last_name, new_name)
    except FileNotFoundError:
        create_log_file(f'Файл {last_name} не найден')
        return False
    except FileExistsError:
        create_log_file(
            f'Не возможно переименовать файл {last_name} в {new_name}! ' +
            'Файл с таким именем уже существует.'
        )
        return False


def get_files(where: str) -> list:
    try:
        return listdir(where)
    except FileNotFoundError:
        create_log_file(
            f'Не возможно загрузить список файлов из директории {where}'
        )
        return []
