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
        return {
            'available': True if user not in self.data.user_list else False
        }

    def post(self, user: str = ''):
        data = dict(request.form)
        add_to_db(self.data, data)
        return self.data.get_by_name(data['username'])
