from sys import argv

from core import create_log_file, get_files, pjoin, load_file, create_file
from launch import main_check
from server import api_check_user, api_login_user, api_save_note, api_get_notes
from client import MyApp

from PySide6 import QtWidgets
from sys import exit

from settings import file_log, Load_User, Post_Note, fold_notes


def main(args: list):
    conf = main_check()
    create_log_file('Application launched successfully', 'info')

    # app = QtWidgets.QApplication([])
    # widget = MyApp(conf)
    # widget.show()
    # exit(app.exec())

    # check_user('test')
    new_user: Load_User = {'username': 'maxbro', 'password': '123123'}

    user = api_login_user(conf['server']['host'], new_user)
    if user is not None:
        pass


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
