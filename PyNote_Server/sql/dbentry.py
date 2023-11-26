from .base import DataBase

from core import create_log, create_token, create_id


def add_to_db(db: DataBase, data: dict) -> bool:
    try:
        while True:
            uid = create_id()
            if uid not in db.id_list:
                data['id'] = uid
                data['token'] = create_token()
                break
        db.add(data)
        return True
    except Exception as err:
        create_log(err, 'error')
        return False
