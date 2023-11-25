import uvicorn
from sys import argv
from fastapi import FastAPI

from core import create_log
from start import main_check
from server import get_local_ip
# from sql import DataBase, add_to_db

# from settings import 


app = FastAPI(title='PyNote Server')


@app.get('/user/{username}')
def get_users(username: str):
    pass


def main(args: list = []):
    conf = main_check()
    create_log('LAUNCHING =========================', 'info')
    # db = DataBase(file_db)

    uvicorn.run(app, host=get_local_ip(), port=conf['SERVER']['PORT'])
    # create_log(f'Server UP at {ip}:{port}', 'info')
    # start_server(ip, conf['app']['server_token'])


if __name__ == '__main__':
    try:
        main(argv)
    except Exception as err:
        create_log(err, 'crit')
