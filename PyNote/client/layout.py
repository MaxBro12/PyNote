from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

from .editor import Editor
from .notelist import NoteList


class Main_Layout(QVBoxLayout):
    def __init__(self, app):
        super().__init__()
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        self.notes_l = Notes_Layout(app, app.config)
        self.addLayout(self.notes_l)


class Notes_Layout(QHBoxLayout):
    def __init__(self, app, conf):
        super().__init__()

        # ! Список заметок
        self.notes = NoteList(app, conf)
        # ! Редактор заметки
        self.edit = Editor()

        self.addLayout(self.notes, 1)
        self.addSpacing(5)
        self.addLayout(self.edit, 0)
