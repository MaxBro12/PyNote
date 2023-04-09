from PySide6 import QtWidgets, QtGui


from core import (
    read,
    write,

    pjoin,
)
from handlers import (
    get_local_notes,
)

from .layout import Main_Layout, Notes_Layout
from .notelist import NoteItem


from settings import (
    file_icon,
    file_conf,
    fold_themes,

    Theme,
)


class MyApp(QtWidgets.QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        self.notes = get_local_notes()

        # ? Топ панель
        self.setWindowIcon(QtGui.QIcon(file_icon))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(self.config['app']['width'], self.config['app']['height'])
        self.setMinimumSize(300, 400)

        # ! Разметка
        self.layout_main = Main_Layout()
        self.setLayout(self.layout_main)
        self.notes_layout = Notes_Layout()
        self.layout_main.addLayout(self.notes_layout)

        # ! Применяем настройки
        self.update_conf(False)

        # ? Загружаем темку
        self.load_theme()

        self.load_notes()

    def update_conf(self, write_to_file: bool = True):
        if write_to_file:
            write(self.config, file_conf)
        self.setWindowOpacity(self.config['app']['opacity'])

    def load_theme(self):
        theme = read(pjoin(fold_themes, self.config['app']['theme']))

        self.setStyleSheet(
            f"background-color: {theme['background']};" +
            f"color: {theme['text_color']};" +
            # f"border-color: {theme['background']};" +
            f"border-style: outset;"
        )

        # ? Переключаем темы у заметок
        self.notes_layout.notes_list.setStyleSheet(
            f"background-color: {theme['side_pannel']};"
        )

    def load_notes(self):
        self.notes = get_local_notes()
        for note in self.notes:
            self.notes_layout.notes_list.column.addWidget(
                NoteItem()
            )

    def open_note(self):
        pass
