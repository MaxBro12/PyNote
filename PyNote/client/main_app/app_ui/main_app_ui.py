from PySide6.QtWidgets import QWidget, QHBoxLayout

from .notelist_ui import NoteListUI
from .editorui import EditorUI

from settings import ALL_MARGINS, ALL_SPASING


class MainAppUI(QWidget):
    def __init__(self, language: str, title_s: int, text_s: int):
        super().__init__()
        self.row = QHBoxLayout()
        self.row.setContentsMargins(ALL_MARGINS, ALL_MARGINS, ALL_MARGINS, ALL_MARGINS)
        self.row.setSpacing(ALL_SPASING)
        self.setLayout(self.row)
        
        # ! Список заметок
        self.notes = NoteListUI()
        # ! Редактор заметки
        self.edit = EditorUI(language, title_s, text_s)

        self.row.addWidget(self.notes, 1)
        self.row.addSpacing(5)
        self.row.addWidget(self.edit, 0)

"""
class MainAppUI2(QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.theme = cast(
            Theme, read(pjoin(fold_themes, self.config['app']['theme']))
        )
        # self.user = login_user(config['server'], config['user'])
        self.notes = get_local_notes()  # + \
        # serv_get_notes(config['server'], self.user)

        # ? Подключение окна настроек
        print('start')
        self.setts_app = App_Settings(self.config, self.theme)
        print('clear')

        # ? Топ панель
        self.setWindowIcon(QtGui.QIcon(file_icon))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(self.config['app']['width'], self.config['app']['height'])
        self.setMinimumSize(300, 400)

        # ! Разметка
        self.layout_m = Main_Layout(self, self.theme)
        self.setLayout(self.layout_m)

        # ! Подключаем основные кнопки и сигналы
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
        self.setts_app.update_conf.connect(self.update_conf())

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

        print('APP COLLING AP')

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
"""
