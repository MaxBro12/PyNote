from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QTextBrowser, QLabel
)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


from settings import (
    file_new_note_icon,
    file_delete_icon,
    file_sync_icon,
)


class NoteItem(QWidget):
    def __init__(self):
        super().__init__()
        # ? Кнопки, текст и тд
        self.text_area = Text()
        self.b_sync = ButtonSunc()
        self.b_delete = ButtonDelete()
        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setSpacing(0)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.addWidget(self.text_area, 1)
        self.row.addWidget(self.b_sync, 0)
        self.row.addWidget(self.b_delete, 0)

        self.setLayout(self.row)

        self.text_area.setText('wtf')

    @property
    def text(self) -> str:
        return self.text_area.text()

    @text.setter
    def text(self, new):
        self.text_area.setText(new)


class EmptyNote(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # ? Кнопки
        self.newn = ButtonNewNote()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setSpacing(0)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.addWidget(self.newn)

        self.setLayout(self.row)


class Text(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(150, 50))


class ButtonNewNote(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(file_new_note_icon))
        # self.setFixedSize(QSize(50, 50))


class ButtonDelete(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(file_delete_icon))
        self.setFixedSize(QSize(50, 50))


class ButtonSunc(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(file_sync_icon))
        self.setFixedSize(QSize(50, 50))
