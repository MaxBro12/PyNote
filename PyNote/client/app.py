from typing import Optional
from PySide6 import (
    QtWidgets,
    QtGui,
)
import PySide6.QtCore
import PySide6.QtWidgets


from core import (
    read,
    write,

    pjoin,
)
from handlers import (
    get_local_notes,
    add_local_note,

    login_user,

    serv_get_notes,
)

from .layout import Main_Layout
from .app_settings import App_Settings


from settings import (
    file_icon,
    file_conf,
    fold_themes,
)
from spec_types import (
    Server_Data,
    User_Data,
    Config,
    Theme,

    cast,
)


class MyAppMain(QtWidgets.QMainWindow):
    def __init__(self, config: Config) -> None:
        super().__init__()
        self.setCentralWidget(MyApp(config))


class MyApp(QtWidgets.QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.theme = cast(
            Theme, read(pjoin(fold_themes, self.config['app']['theme']))
        )
        # self.user = login_user(config['server'], config['user'])
        self.notes = get_local_notes()  # + \
        # serv_get_notes(config['server'], self.user)

        # ? Топ панель
        self.setWindowIcon(QtGui.QIcon(file_icon))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(self.config['app']['width'], self.config['app']['height'])
        self.setMinimumSize(300, 400)

        # ! Разметка
        self.layout_m = Main_Layout(self, self.theme)
        self.setLayout(self.layout_m)

        # ! Подключаем основные кнопки
        self.layout_m.notes_l.notes.settings.add_note.clicked.connect(
            self.add_note
        )
        self.layout_m.notes_l.notes.settings.settings.clicked.connect(
            self.open_settings
        )
        self.layout_m.notes_l.notes.list.itemClicked.connect(
            self.load_note
        )
        self.layout_m.notes_l.edit.newNote.connect(
            self.add_empty_note
        )

        # ! Применяем настройки
        self.update_conf(False)

        # ? Загружаем темку
        self.load_theme()

        self.update_notes()
        self.setts_app = None

    def update_conf(self, write_to_file: bool = True):
        # ? Запись в файл
        if write_to_file:
            write(self.config, file_conf)

        # ? Обновления параметров
        self.setWindowOpacity(self.config['app']['opacity'])

    def load_theme(self):
        self.theme = cast(
            Theme, read(pjoin(fold_themes, self.config['app']['theme']))
        )

        self.setStyleSheet(
            f"background-color: {self.theme['background']};" +
            f"color: {self.theme['text_color']};" +
            # f"border-color: {theme['background']};" +
            f"border-style: outset;"
        )

        # ? Переключаем темы у заметок
        self.layout_m.notes_l.notes.list.setStyleSheet(
            f"background-color: {self.theme['side_panel']};"
        )
        self.layout_m.notes_l.notes.settings.setStyleSheet(
            f"background-color: {self.theme['side_panel']};"
        )

    def update_notes(self):
        self.notes = get_local_notes()
        for note in self.notes:
            self.add_note(
                note['name'].split('.')[0],
                note['inner']
            )

    # ! ================================ SLOTS ================================
    def add_note(self, name: str = '', inner: str = ''):
        self.layout_m.notes_l.notes.add(name, inner)

    def add_empty_note(self, name):
        widget = self.layout_m.notes_l.notes.spec_add(name)
        self.layout_m.notes_l.edit.update_info(widget)

    def load_note(self, item: QtWidgets.QListWidgetItem):
        widget = self.layout_m.notes_l.notes.list.itemWidget(item)
        self.layout_m.notes_l.edit.update_info(widget)

    # ! Слоты для настроек
    def open_settings(self):
        if self.setts_app is None:
            self.setts_app = App_Settings(self.config, self.theme)
        self.setts_app.show()
