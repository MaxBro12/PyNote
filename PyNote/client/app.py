from PySide6 import (
    QtWidgets,
    QtGui,
)


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
from .notelist import NoteItem


from settings import (
    file_icon,
    file_conf,
    fold_themes,
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
        self.layout_m = Main_Layout()
        self.setLayout(self.layout_m)
        self.notes_l = Notes_Layout(self)
        self.layout_m.addLayout(self.notes_l)

        # ! Подключаем основные кнопки
        self.notes_l.notes.settings.add_note.clicked.connect(
            self.add_note
        )
        self.notes_l.notes.list.itemClicked.connect(
            self.load_note
        )

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
        self.notes_l.notes.list.setStyleSheet(
            f"background-color: {theme['side_pannel']};"
        )
        self.notes_l.notes.settings.setStyleSheet(
            f"background-color: {theme['side_pannel']};"
        )

    def update_notes(self):
        self.notes = get_local_notes()
        for note in self.notes:
            self.add_note(
                note['name'].split('.')[0],
                note['inner']
            )

    def add_note(self, name: str = '', inner: str = ''):
        self.notes_l.notes.add(name, inner)
        # add_local_note(f'new-{len(self.notes)}')
        # self.update_notes()

    def load_note(self, item: QtWidgets.QListWidgetItem):
        widget = self.notes_l.notes.list.itemWidget(item)
        self.notes_l.edit.update_info(widget)
