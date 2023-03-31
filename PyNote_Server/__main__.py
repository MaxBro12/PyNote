from core import create_log_file
from launch import main_check
from sql import DataBase, add_to_db
from server import UsersResources


from sys import argv
from flask import Flask
from flask_restful import Api


from settings import file_db, host, port, debug


def main(args: list = []):
    conf = main_check()
    db = DataBase(file_db)
    create_log_file('Server UP', 'info')

    # ! Запуск фласка
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(UsersResources, "/api/test")
    app.run(debug=debug, port=port, host=host)
    # api.init_app(app)


if __name__ == '__main__':
    try:
        # argv.pop()
        main(argv)

    except Exception as err:
        create_log_file(err, 'crit')
