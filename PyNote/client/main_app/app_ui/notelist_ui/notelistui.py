from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
)
from PySide6.QtCore import QSize

from .noteitemui import NoteItemUI
from .notemenuui import NoteMenuUI

from settings import NOTE_LIST_L_PANNEL_SIZE
from settings import ALL_MARGINS, ALL_SPASING


class NoteListUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(NOTE_LIST_L_PANNEL_SIZE)

        self.col = QVBoxLayout()
        self.col.setContentsMargins(ALL_MARGINS)
        self.col.setSpacing(ALL_SPASING)
        self.setLayout(self.col)

        # Список заметок
        self.note_l = QListWidget()
        self.note_l.setMaximumWidth(NOTE_LIST_L_PANNEL_SIZE - 5)
        self.col.addWidget(self.note_l)

        # Панель управления
        self.menu = NoteMenuUI()
        self.col.addWidget(self.menu)

