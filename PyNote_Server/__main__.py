from core import create_log_file
from launch import main_check
from sql import DataBase, add_to_db
from server import start_server, get_local_ip


from sys import argv


from settings import file_db, host, port, debug


def main(args: list = []):
    conf = main_check()
    # db = DataBase(file_db)
    create_log_file('Server UP', 'info')

    start_server(get_local_ip())


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)

    except Exception as err:
        create_log_file(err, 'crit')
