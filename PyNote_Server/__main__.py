from sys import argv


from core import create_log_file
from launch import main_check
from sql import DataBase, add_to_db
from server import start_server, get_local_ip


from settings import file_db, host, port, debug


def main(args: list = []):
    conf = main_check()
    # db = DataBase(file_db)

    ip = get_local_ip()
    create_log_file(f'Server UP at {ip}:{port}', 'info')
    start_server(ip)


if __name__ == '__main__':
    try:
        argv.pop()
        main(argv)

    except Exception as err:
        create_log_file(err, 'crit')
