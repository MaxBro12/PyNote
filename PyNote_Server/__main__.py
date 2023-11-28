import uvicorn
from sys import argv
from fastapi import FastAPI

from core import create_log
from start import main_check
# from server import get_local_ip
from sql import DataBase

#from settings import FILE_DB


# app = FastAPI(title='PyNote Server')
# config = dict()
# db = DataBase(FILE_DB)


# @app.get('/notes')
# def get_users(token: str, username: str, password: str):
#     if config['token'] == token:
#         if username in db.users:
#             #if password == 
#             pass
# 
# 
# @app.get('/user')
# def new_user(token: str, username: str, password: str):
#     if config['token'] == token:
#         if username in db.users:
#             return {'msg': 'exist'}
#         else:
#             db.add({})


def main(args: list = []):
    config = main_check()
    create_log('LAUNCHING =========================', 'info')

    
    # create_log(f'Server UP at {ip}:{port}', 'info')
    # start_server(ip, conf['app']['server_token'])


if __name__ == '__main__':
    try:
        main(argv)
    except Exception as err:
        create_log(err, 'crit')
