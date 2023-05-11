from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout

from .editor import Editor
from .notelist import NoteList

from spec_types import Theme


class Main_Layout(QVBoxLayout):
    def __init__(self, app, theme: Theme):
        super().__init__()
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        self.notes_l = Notes_Layout(app, theme, app.config)
        self.addLayout(self.notes_l)


class Notes_Layout(QHBoxLayout):
    def __init__(self, app, theme, conf):
        super().__init__()

        # ! Список заметок
        self.notes = NoteList(app, theme, conf)
        # ! Редактор заметки
        self.edit = Editor(conf)

        self.addLayout(self.notes, 1)
        self.addSpacing(5)
        self.addLayout(self.edit, 0)
