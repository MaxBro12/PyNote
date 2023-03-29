from sys import argv

from core import create_log_file
from launch import main_check
from sql import DataBase, add_to_db

from settings import file_db


def main(args: list = []):
    conf = main_check()
    db = DataBase(file_db)
    create_log_file('Server UP', 'info')

    a = {'username': 'test', 'password': '123123'}

    add_to_db(db, a)
    db.remove(70486)


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)
    except Exception as err:
        create_log_file(err, 'crit')
