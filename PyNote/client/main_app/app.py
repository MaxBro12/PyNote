from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from .app_ui import MainAppUI, NoteItemUI
from ..settings_app import SettingsWindow
from ..warning_app import WarningApp 
from core import (
    create_log,

    pjoin,
    wayfinder,

    read_toml,

    save_local_note,
    get_local_notes,
    add_local_note,
    remove_local_note,
    load_local_note,
    rename_local_note,
)

from settings import (
    DIR_THEMES,
    FILE_SETTINGS,
    FILE_APP_ICON,
    NOTE_LIST_ITEM,
)


class MyAppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка конфига
        self.config = read_toml(FILE_SETTINGS) 
        
        # Доп окна
        self.warning = None
        self.settings = None
        
        # Рамка
        self.setWindowIcon(QIcon(FILE_APP_ICON))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(
            self.config['MAIN']['width'], self.config['MAIN']['height']
        )
        self.setMinimumSize(300, 400)

        # Тема
        self.load_theme()

        # Главный виджет
        self.main = MainAppUI(
            self.config['MAIN']['lang'],
            self.config['MAIN']['font_editor_title_size'],
            self.config['MAIN']['font_editor_text_size'],
        )
        self.setCentralWidget(self.main)

        # ! Подключаем кнопки и сигналы
        self.main.notes.menu.set_b.clicked.connect(self.show_settings)
        self.main.notes.menu.add_note_b.clicked.connect(self.add_note)
        self.main.notes.note_l.itemClicked.connect(self.load_note)
        
        self.main.edit.title_i.editingFinished.connect(self.save_note)
        self.main.edit.editor_i.textChanged.connect(self.save_note)

        # ! Заметки локальные
        self.update_notes()

    # MAIN ====================================================================
    def show_settings(self):
        if self.settings is None:
            self.settings = SettingsWindow()
            create_log('Show settings', 'debug')
            self.settings.show()
        else:
            self.settings = None

    def show_warning(self, msg: str):
        if self.warning is None:
            self.warning = WarningApp(msg)
            create_log(f'Show Warning:\n{msg}', 'debug')
            self.warning.show()
        else:
            self.warning = None

    def load_config(self):
        self.config = read_toml(FILE_SETTINGS)

    def load_theme(self):
        # Проверяем если значение вообще не пустное
        if self.config['MAIN']['theme']:
            way = pjoin(DIR_THEMES, self.config['MAIN']['theme'])
            # Проверяем существование файла до открытия
            if wayfinder(way):
                with open(way) as f:
                    self.setStyleSheet(f.read())

    # NOTES ===================================================================
    def update_notes(self):
        # Очищаем список заметок
        self.main.notes.note_l.clear()
        # Получаем список всех локальных заметок
        lnotes = get_local_notes()
        for i in lnotes:
            item = QListWidgetItem(self.main.notes.note_l)
            item.setSizeHint(NOTE_LIST_ITEM)
            widget = NoteItemUI(i['name'], item, self.config['MAIN']['lang'])
            self.main.notes.note_l.setItemWidget(
                item,
                widget
            )
            # Подключаем item
            widget.del_s.connect(self.del_note)

    def add_note(self):
        name = f"New-{len(get_local_notes())}"
        add_local_note(name, '')
        self.update_notes()

    def save_note(self):
        if self.main.edit.title_i.text() != self.main.edit.title_l:
            rename_local_note(
                self.main.edit.title_l,
                self.main.edit.title_i.text()
            )
            self.main.edit.title_l = self.main.edit.title_i.text()
        add_local_note(
            self.main.edit.title_i.text(),
            self.main.edit.editor_i.toMarkdown()
        )
        self.update_notes()

    def load_note(self, item):
        name = self.main.notes.note_l.itemWidget(
            item
        ).name.text().removeprefix('  ')
        self.main.edit.title_l = name
        self.main.edit.title_i.setText(name)
        self.main.edit.editor_i.setText(load_local_note(name))

    def del_note(self, item):
        # Получить количество строк, соответствующих item
        row = self.main.notes.note_l.indexFromItem(item).row()
        # Удаляем заметку
        remove_local_note(
            self.main.notes.note_l.itemWidget(
                item
            ).name.text().removeprefix('  ')
        )
        # Удалить item
        item = self.main.notes.note_l.takeItem(row)
        # Удалить widget
        self.main.notes.note_l.removeItemWidget(item)

        self.update_notes()

    # SERVER ==================================================================
