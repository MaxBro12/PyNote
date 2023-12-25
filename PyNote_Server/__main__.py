import uvicorn
from sys import argv
from fastapi import FastAPI
from server.local import get_local_ip

from core import create_log
from start import main_check
from server.routers import users, notes, status


def main(args: list):
    create_log('LAUNCHING =========================', 'info')
    ip = get_local_ip()
    config = main_check()

    app = FastAPI(title='PyNote Server')
    app.include_router(users.router)
    app.include_router(notes.router)
    app.include_router(status.router)

    create_log(f'Server UP at {ip}:{config['SERVER']['PORT']}', 'info')
    uvicorn.run(app, host=ip, port=config['SERVER']['PORT'])


if __name__ == '__main__':
    try:
        main(argv)
    except Exception as err:
        create_log(err, 'crit')
