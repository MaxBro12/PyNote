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


class NoteListUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(NOTE_LIST_L_PANNEL_SIZE)

        self.col = QVBoxLayout()
        self.setLayout(self.col)

        # Список заметок
        self.note_l = QListWidget()
        self.col.addWidget(self.note_l)

        # Панель управления
        self.menu = NoteMenuUI()
        self.col.addWidget(self.menu)

