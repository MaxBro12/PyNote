from sys import argv

from core import create_log_file
from launch import main_check
from sql import DataBase

from settings import file_db


def main(args: list = []):
    conf, data = main_check()
    create_log_file('Server UP', 'info')
    data = DataBase(file_db)

    a = {
        'id': 70486,
        'username': 'maxbro',
        'password': '123123',
        'token': '1dsg3j1po3'
    }
    b = {
        'id': 70426,
        'username': 'maxbro2',
        'password': '123123',
        'token': '1dsg3j1po3'
    }

    data.add(a)
    data.add(b)

    data.remove(70426)
    data.remove(70426)
    print(data.user_list)


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)
    except Exception as err:
        create_log_file(err, 'crit')
