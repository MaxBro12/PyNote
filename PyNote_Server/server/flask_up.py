from flask import Flask
from flask_restful import Api

from .source import (
    NewUserResources,
    UsersResources,
)

from settings import (
    debug,
    host,
    port,

    api_new_user_1,
    api_new_user_2,
    api_new_user_3,
    api_user_data,
)


def start_server(ip):
    # ! Запуск фласка
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        NewUserResources,
        api_new_user_1,
        api_new_user_2,
        api_new_user_3,
    )
    api.add_resource(UsersResources, api_user_data)

    app.run(debug=debug, port=port, host=ip)
