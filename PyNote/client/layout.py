from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

from .editor import Editor
from .notelist import NoteList


class Main_Layout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)


class Notes_Layout(QHBoxLayout):
    def __init__(self, app):
        super().__init__()

        # ! Список заметок
        self.notes_list = NoteList(app)
        # ! Редактор заметки
        self.note_edit = Editor()

        self.addWidget(self.notes_list, 1)
        self.addLayout(self.note_edit, 0)
