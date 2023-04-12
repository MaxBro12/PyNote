from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel
)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


from settings import (
    file_new_note_icon,
    file_delete_icon,
    file_sync_icon,
)


class NoteItem(QWidget):
    def __init__(self, text: str = '', sync: bool = True):
        super().__init__()
        # ? Кнопки, текст и тд
        self.text_area = Text()
        self.b_sync = ButtonSunc()
        self.b_delete = ButtonDelete()
        self.__sync = sync
        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setSpacing(0)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.addWidget(self.text_area, 1)
        self.row.addWidget(self.b_sync, 0)
        self.row.addWidget(self.b_delete, 0)

        self.setLayout(self.row)
        self.setFixedSize(QSize(250, 50))

        self.text_area.setText(text)

    @property
    def text(self) -> str:
        return self.text_area.text()

    @text.setter
    def text(self, new_text: str):
        self.text_area.setText(new_text)


class EmptyNote(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # ? Кнопки
        self.newn = ButtonNewNote()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setSpacing(0)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.addWidget(self.newn, 0)

        self.setMinimumSize(QSize(200, 50))

        self.setLayout(self.row)


class Text(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(150, 50))
        self.setTextMargins(10, 0, 0, 0)
        self.setMaxLength(20)  # ? Пока ограничим размер текстового поля


class ButtonNewNote(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(file_new_note_icon))
        self.setMinimumSize(QSize(50, 50))


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
