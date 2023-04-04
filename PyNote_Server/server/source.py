from flask_restful import Resource, reqparse
from flask import request


from core import create_log_file
from sql import DataBase, add_to_db


from settings import file_db


class Data():
    def __init__(self) -> None:
        self.data = DataBase(file_db)


class NotesResources(Resource, Data):
    def __init__(self) -> None:
        super().__init__()

    def get(self, token: str):
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

    def get(self, user: str):
        req = dict(request.form)
        data = self.data.get_by_name(req['username'])
        if data is not None:
            if req['password'] == data['password']:
                return data
        else:
            return {'user': 'User not found'}

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
        test = list(request.access_route)
        create_log_file(test[0], 'debug')
        return {
            'available': True if user not in self.data.user_list else False
        }

    def post(self, user: str = ''):
        data = dict(request.form)
        add_to_db(self.data, data)
        return self.data.get_by_name(data['username'])
