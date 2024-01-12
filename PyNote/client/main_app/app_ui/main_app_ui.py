from PySide6.QtWidgets import QWidget, QHBoxLayout

from .notelist_ui import NoteListUI
from .editorui import EditorUI

from settings import ALL_MARGINS, ALL_SPASING


class MainAppUI(QWidget):
    def __init__(self, language: str, title_s: int, text_s: int):
        super().__init__()
        self.row = QHBoxLayout()
        self.row.setContentsMargins(ALL_MARGINS)
        self.row.setSpacing(ALL_SPASING)
        self.setLayout(self.row)
        
        # ! Список заметок
        self.notes = NoteListUI()
        # ! Редактор заметки
        self.edit = EditorUI(language, title_s, text_s)

        self.row.addWidget(self.notes, 1)
        self.row.addSpacing(5)
        self.row.addWidget(self.edit, 0)
