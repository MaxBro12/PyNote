from PySide6 import QtWidgets, QtGui


from core import (
    read,
    write,

    pjoin,
)
from handlers import (
    get_local_notes,
    add_local_note,
)

from .layout import Main_Layout, Notes_Layout
from .notelist import NoteItem, EmptyNote


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
        self.notes_layout = Notes_Layout(self)
        self.layout_main.addLayout(self.notes_layout)

        # ! Применяем настройки
        self.update_conf(False)

        # ? Загружаем темку
        self.load_theme()

        self.update_notes()

    def update_conf(self, write_to_file: bool = True):
        # ? Запись в файл
        if write_to_file:
            write(self.config, file_conf)

        # ? Обновления параметров
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

    def update_notes(self):
        self.notes = get_local_notes()
        self.notes_layout.notes_list.notes = [
            NoteItem(n['name'].split('.')[0]) for n in self.notes
        ]
        self.notes_layout.notes_list.setts.newn.clicked.connect(self.add_note)

    def add_note(self):
        add_local_note(f'new-{len(self.notes)}')
        self.update_notes()
