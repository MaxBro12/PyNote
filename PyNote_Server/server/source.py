from flask_restful import Resource, reqparse


from core import create_log_file
from sql import DataBase, add_to_db


from settings import file_db


class Data():
    def __init__(self) -> None:
        self.data = DataBase(file_db)


class NotesResources(Resource, Data):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        pass

    def post(self):
        pass

    def pul(self):
        pass

    def delete(self):
        pass


class UsersResources(Resource, Data):
    def __init__(self):
        super().__init__()

    def get(self, uid: int):
        return self.data.get(uid), 200

    def post(self):
        pass

    def pul(self):
        pass

    def delete(self):
        pass


class NewUserResources(Resource, Data):
    def __init__(self) -> None:
        super().__init__()

    def get(self, user: str = ''):
        return {'aval': True if user not in self.data.user_list else False}

    def post(self, user: str = ''):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        param = parser.parse_args()
        add_to_db(self.data, param)
        create_log_file(param, 'debug')
        return {'message': "Got it"}
