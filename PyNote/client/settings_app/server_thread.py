from PySide6.QtCore import QObject, Signal
from server.services import server_get_status
from server.users import server_new_user, server_delete_user
from spec_types import User


class WorkerServerSt(QObject):
    finished = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.server_st = False

    def get_server_st(self, host: str | None = None):
        if host is None:
            return None
        self.server_st = server_get_status(host)

    def create_new_user(
            self, 
            host: str | None = None,
            user: User | None = None,
    ):
        if host is None or user is None:
            return None
        server_new_user(host, user)

    def delete_new_user(
            self, 
            host: str | None = None,
            user: User | None = None,
    ):
        if host is None or user is None:
            return None
        server_delete_user(host, user)
