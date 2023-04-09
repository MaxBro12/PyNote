from flask import Flask
from flask_restful import Api

from .source import (
    NotesResources,
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
    api_user_data_1,
    api_user_data_2,
    api_user_data_3,
    api_notes_1,
    api_notes_2,
    api_notes_3,
)


def start_server(ip: str, token: str):
    # ! Запуск фласка
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(
        NewUserResources,
        '/' + token + '/' + api_new_user_1,
        '/' + token + '/' + api_new_user_2,
        '/' + token + '/' + api_new_user_3,
    )

    api.add_resource(
        UsersResources,
        '/' + token + '/' + api_user_data_1,
        '/' + token + '/' + api_user_data_2,
        '/' + token + '/' + api_user_data_3,
    )

    api.add_resource(
        NotesResources,
        '/' + token + '/' + api_notes_1,
        '/' + token + '/' + api_notes_2,
        '/' + token + '/' + api_notes_3,
    )

    app.run(debug=debug, port=port, host=ip)
