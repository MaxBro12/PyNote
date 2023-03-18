import logging
from typing import Union
from os import get_terminal_size


def error_found(err):
    print(f"{'=' * (get_terminal_size()[0] - 1)}\nError logged:\n{err}")
    create_log_file(err)


def create_log_file(log: Union[Exception, str], levelname: str = 'debug'):
    """Добовляем в лог данные log с указанием типа уровня:
    - debug - дебаг
    - warning - предупреждение
    - info - информация
    - error - ошибка
    - crit - критическая ошибка"""
    logging.basicConfig(
        level=logging.DEBUG,
        filename="error.log",
        filemode="a",
        format="%(asctime)s %(levelname)s %(message)s",
    )
    log_exc = False
    if type(log) == Exception:
        log_exc = True
    match levelname:
        case 'debug':
            logging.debug(log, exc_info=log_exc)
        case 'warning':
            logging.warning(log, exc_info=log_exc)
        case 'info':
            logging.info(log, exc_info=log_exc)
        case 'error':
            logging.error(log, exc_info=log_exc)
        case 'crit':
            logging.critical(log, exc_info=log_exc)
