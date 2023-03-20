from toml import load, dump
from ..debug import create_log_file


def read(way: str) -> dict:
    """Считываем файл по пути way формата .toml и возвращаем словарь"""
    return load(way)


def write(dictionary: dict, way: str):
    """Записываем словарь dictionary в toml файл по пути way"""
    with open(way, 'w') as toml_file:
        dump(dictionary, toml_file)
