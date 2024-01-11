from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidgetItem,
)
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Signal

from lang import lang
from settings import (
    ALL_MARGINS,
    ALL_SPASING,
    NOTE_LIST_ITEM_B,
    NOTE_LIST_ITEM_L,
    NOTE_LIST_ITEM_ICON
)


class NoteItemUI(QWidget):
    del_s = Signal(QListWidgetItem)

    def __init__(self, name: str, item: QListWidgetItem, language: str):
        super().__init__()
        self.__item = item

        # Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(ALL_MARGINS)
        self.row.setSpacing(ALL_SPASING)
        self.setLayout(self.row)

        # Имя
        self.name = QLabel(f"  {name}")
        self.name.setFixedSize(NOTE_LIST_ITEM_L)
        self.row.addWidget(self.name)

        # Синхронизация
        self.sync_b = QPushButton()
        self.sync_b.setObjectName('sync_b')
        self.sync_b.setToolTip(lang[language]['sync_but'])
        self.sync_b.setIconSize(NOTE_LIST_ITEM_ICON)
        self.sync_b.setFixedSize(NOTE_LIST_ITEM_B)
        self.row.addWidget(self.sync_b)

        # Удаление
        self.del_b = QPushButton()
        self.del_b.setObjectName('del_b')
        self.del_b.setToolTip(lang[language]['delete_but'])
        self.del_b.setIconSize(NOTE_LIST_ITEM_ICON)
        self.del_b.setFixedSize(NOTE_LIST_ITEM_B)
        self.del_b.clicked.connect(self.del_e)
        self.row.addWidget(self.del_b)
    
    def del_e(self):
        self.del_s.emit(self.__item)
