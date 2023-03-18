from sys import argv

from core import create_log_file
from launch import main_check


def main(args: list = []):
    conf = main_check()
    create_log_file('App launched', 'info')


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)
    except Exception as err:
        create_log_file(err, 'crit')
        print(
            "Во время работы приложния обнаружена ошибка!\n" +
            "Отправьте файл error.log разработчику"
        )
