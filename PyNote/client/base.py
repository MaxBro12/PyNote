from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QPalette, QColor
from os import path

from core import read
from handlers import get_notes

from .editor import Editor
from .notelist import NoteList

from settings import file_icon, fold_themes


class MyApp(QtWidgets.QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        self.notes = get_notes()

        self.setWindowOpacity(0.98)

        # ? Топ панель
        self.setWindowIcon(QtGui.QIcon(file_icon))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(self.config['app']['width'], self.config['app']['height'])
        self.setMinimumSize(300, 400)
        # self.setFixedSize()
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # ? Список заметок
        self.notes_list = NoteList()
        self.notes_list.setMaximumWidth(300)
        self.notes_list.setMinimumWidth(0)

        # ? Редактор заметки
        self.note_edit = Editor()
        # self.note_edit.setMinimumWidth(300)

        # ? Разметка ==========================================================
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.setSpacing(0)
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_main)

        # self.layout_top = QtWidgets.QHBoxLayout()
        # self.layout_main.addLayout(self.layout_top)
        # self.layout_top.setSpacing(0)
        # self.layout_top.setContentsMargins(0, 0, 0, 0)
        # self.layout_top.addWidget(Color('blue'))
        # self.layout_top.addWidget(Color('blue'))
        # self.layout_top.addWidget(Color('blue'))

        self.layout_notes = QtWidgets.QHBoxLayout()
        self.layout_main.addLayout(self.layout_notes)
        self.layout_notes.setSpacing(0)
        self.layout_notes.setContentsMargins(0, 0, 0, 0)
        self.layout_notes.addWidget(self.notes_list)
        self.layout_notes.addLayout(self.note_edit)

        # ? Загружаем темку
        self.load_theme()

        self.load_notes()

    def load_theme(self):
        theme = read(path.join(fold_themes, self.config['app']['theme']))

        self.setStyleSheet(
            f"background-color: {theme['back']};" +
            f"color: {theme['text']};"
            # "border-width: 0px;" +
            # f"border-color: {theme['back']};"
        )

        # ? Переключаем темы у заметок
        self.notes_list.setStyleSheet(
            f"background-color: {theme['side']};"
        )
        # for i in self.notes_list:
        #     pass

    def load_notes(self):
        self.notes = get_notes()
        for note in self.notes:
            self.notes_list.addItem(QtWidgets.QListWidgetItem(note))

    def open_note(self):
        pass


class Color(QtWidgets.QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
