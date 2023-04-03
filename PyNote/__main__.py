from sys import argv

from core import create_log_file
from launch import main_check
from client import MyApp
from server import check_user, create_user

from PySide6 import QtWidgets
from sys import exit

from settings import file_log


def main(args: list = []):
    conf = main_check()
    create_log_file('Application launched successfully', 'info')

    # app = QtWidgets.QApplication([])
    # widget = MyApp(conf)
    # widget.show()
    # exit(app.exec())

    # check_user('test')
    # `check_user('maxbro')
    create_user('maxbro2', '123123')


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)
    except Exception as err:
        create_log_file(err, 'crit')
        print(
            "Во время работы приложния обнаружена ошибка!\n" +
            f"Отправьте файл {file_log} разработчику."
        )
