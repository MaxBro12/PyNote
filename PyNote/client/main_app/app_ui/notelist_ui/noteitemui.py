from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidgetItem,
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from settings import FONT_NOTES_LIST_SIZE, FONT_NOTES_LIST_FAMILY
from lang import lang


class NoteItemUI(QWidget):
    def __init__(self, name: str, language: str):
        super().__init__()

        # Разметка
        self.row = QHBoxLayout()
        self.setLayout(self.row)
 
        # Имя
        self.name = QLabel(name)
        self.row.addWidget(self.name)

        # Синхронизация
        self.sync_b = QPushButton()
        self.row.addWidget(self.sync_b)
        self.sync_b.setToolTip(lang[language]['sync_b_but'])
        # self.sync_b.clicked.connect(self.slot_sync_b)
        # self.sync_b.setIcon(QIcon(theme['file_sync_icon']))
        self.sync_b.setIconSize(QSize(20, 20))
        self.sync_b.setFixedSize(QSize(50, 50))

        # Удаление
        self.del_b = QPushButton()
        self.del_b.setToolTip(lang[language]['delete_but'])
        # self.del_b.clicked.connect(self.slot_delete)
        # self.del_b.setIcon(QIcon(theme['file_delete_icon']))
        self.del_b.setIconSize(QSize(20, 20))
        self.del_b.setFixedSize(QSize(50, 50))

        self.row.addWidget(self.del_b)
