from flask_restful import Resource, reqparse
from flask import request


from core import create_log_file
from sql import DataBase, add_to_db
from handlers import (
    get_notes,

    delete_note,
    create_note,

    create_userfolder,
    delete_userfolder,
)


from settings import file_db


class Data():
    def __init__(self) -> None:
        self.data = DataBase(file_db)


class NotesResources(Resource, Data):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        req = dict(request.form)
        data = self.data.get(int(req['id']))
        if data is not None:
            if data['token'] == req['token']:
                return {'log': get_notes(data['username'])}
            return {'log': 'token is not yours'}
        return {'log': 'Data not found'}

    def post(self):
        req = dict(request.form)
        data = self.data.get(int(req['id']))
        if data is not None:
            create_log_file(f'Creating note {req["name"]}', 'debug')
            if create_note(
                data['username'], {'name': req['name'], 'inner': req['inner']}
            ):
                return {'log': True}
            return {'log': False}
        return {'log': 'User not found'}

    def pul(self):
        pass

    def delete(self, user: str):
        req = dict(request.form)
        data = self.data.get(int(req['id']))
        if data is not None:
            return {'log': delete_note(
                data['username'], req['name']
            )}
        return {'log': 'Error note not found'}


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
            return {'log': 'User not found'}

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
            'log': True if user not in self.data.user_list else False
        }

    def post(self, user: str = ''):
        data = dict(request.form)
        add_to_db(self.data, data)
        create_userfolder(data['username'])
        return self.data.get_by_name(data['username'])
