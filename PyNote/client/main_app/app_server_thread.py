from PySide6.QtCore import QObject, Signal
from server.services import server_get_status
from server.notes import server_get_notes, server_add_note, server_delete_note
from spec_types import User, Note


class WorkerServerSt(QObject):
    finished = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.server_st = False
        self.notes = []

    def get_server_st(self, host: str | None = None):
        if host is None:
            return None
        self.server_st = server_get_status(host)

    def get_all_notes(self, host: str | None = None, user: User | None = None):
        if host is None or user is None:
            return None
        self.notes = server_get_notes(host, user)
        return self.notes

    def add_note(
            self,
            host: str | None = None,
            user: User | None = None,
            note: Note | None = None
    ):
        if host is None or user is None or note is None:
            return None
        server_add_note(host, user, note)

    def delete_note(
            self,
            host: str | None = None,
            user: User | None = None,
            note: Note | None = None
    ):
        if host is None or user is None or note is None:
            return None
        note.inner = ''
        server_delete_note(host, user, note)
