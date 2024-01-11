from typing import Optional
from PySide6.QtCore import QObject, Signal
from server.services import server_get_status


class WorkerServerSt(QObject):
    finished = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.server_st = False

    def get_server_st(self, host: str | None = None):
        if host is None:
            return None
        self.server_st = server_get_status(host)
