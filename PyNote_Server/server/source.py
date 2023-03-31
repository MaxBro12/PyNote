from flask_restful import Resource, Api


# from sql import DataBase


class NotesResources(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def pul(self):
        pass

    def delete(self):
        pass


class UsersResources(Resource):
    def get(self):
        return {'test': 'da', 'wtf': 'hueta'}

    def post(self):
        pass

    def pul(self):
        pass

    def delete(self):
        pass
