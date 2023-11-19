from sys import argv, exit

from PySide6.QtWidgets import QApplication

from client import ErrorApp
from core import create_log
from start import main_check


def main(args: list):
    # ? Загрузка
    main_check()
    for i in range(1_000_000):
        create_log(f'{i}', 'crit')

    # ? Запуск приложения
    # app = QApplication(args)
    # widget = MyApp(conf)
    # widget.show()
    # exit(app.exec())


if __name__ == '__main__':
    try:
        main(argv)
    except Exception as err:
        create_log(err, 'crit')

        if QApplication.instance() is None:
            app = QApplication([])
        widget = ErrorApp(err)
        widget.show()
        exit(QApplication.exec())

