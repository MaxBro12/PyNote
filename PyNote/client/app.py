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

    login_user,

    serv_get_notes,
)

from .layout import Main_Layout


from settings import (
    file_icon,
    file_conf,
    fold_themes,

    Server_Data,
    User_Data,

    Config
)


class MyApp(QtWidgets.QWidget):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        # self.user = login_user(config['server'], config['user'])
        self.notes = get_local_notes() #+ \
            #serv_get_notes(config['server'], self.user)

        # ? Топ панель
        self.setWindowIcon(QtGui.QIcon(file_icon))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(self.config['app']['width'], self.config['app']['height'])
        self.setMinimumSize(300, 400)

        # ! Разметка
        self.layout_m = Main_Layout(self)
        self.setLayout(self.layout_m)

        # ! Подключаем основные кнопки
        self.layout_m.notes_l.notes.settings.add_note.clicked.connect(
            self.add_note
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
        self.layout_m.notes_l.notes.list.setStyleSheet(
            f"background-color: {theme['side_pannel']};"
        )
        self.layout_m.notes_l.notes.settings.setStyleSheet(
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
        self.layout_m.notes_l.notes.add(name, inner)

    def add_empty_note(self, name):
        widget = self.layout_m.notes_l.notes.spec_add(name)
        self.layout_m.notes_l.edit.update_info(widget)

    def load_note(self, item: QtWidgets.QListWidgetItem):
        widget = self.layout_m.notes_l.notes.list.itemWidget(item)
        self.layout_m.notes_l.edit.update_info(widget)
