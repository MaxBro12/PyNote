from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
)
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon, QFont


class NoteMenuUI(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.row = QHBoxLayout()
        self.setLayout(self.row)

        # Новая заметка
        self.add_note_b = QPushButton()
        # self.add_note_b.setToolTip(lang[language]['add_but'])
        # self.add_note_b.setIcon(QIcon(theme['file_new_note_icon']))
        # self.add_note_b.setIconSize(QSize(30, 30))
        self.add_note_b.setMinimumSize(QSize(50, 50))

        # Настройки
        self.set_b = QPushButton()
        # self.set_b.setToolTip(lang[language]['settings_but'])
        # self.settings.setIcon(QIcon(theme['file_settings_icon']))
        # self.settings.setIconSize(QSize(25, 25))
        self.set_b.setMinimumSize(QSize(50, 50))

