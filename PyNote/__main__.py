from sys import argv

from core import create_log_file
from launch import main_check
from handlers import login_user
from client import MyApp

from PySide6 import QtWidgets
from sys import exit

from settings import file_log, Server_Data, Load_User


def main(args: list):
    # ? Загрузка
    conf = main_check()
    if conf['server']['token'] == '':
        conf['server']['token'] = 'a'
    create_log_file('===== Application launched successfully =====', 'info')

    # ? Сервер

    # ? Запуск приложения
    app = QtWidgets.QApplication(args)
    widget = MyApp(conf)
    widget.show()
    exit(app.exec())


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
