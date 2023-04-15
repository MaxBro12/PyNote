from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,

    QListWidgetItem,
)
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon


from handlers import (
    rename_local_note,
    remove_local_note,
)


from settings import (
    file_new_note_icon,
    file_delete_icon,
    file_sync_icon,
    file_settings_icon,
)
from language import lang


class NoteItem(QWidget):
    itemDeleted = Signal(QListWidgetItem)
    itemSync = Signal(QListWidgetItem)

    def __init__(self, name: str, inner: str, item, app, language: str = 'ru'):
        super().__init__()
        self.__item = item
        self.name = name
        self.inner = inner
        self.sync_s = False
        self.parent = app

        # ? Текст
        self.text_e = QLabel('  ' + name)  # QLineEdit
        self.text_e.setFixedSize(QSize(150, 50))
        self.text_e.setContentsMargins(5, 0, 0, 0)

        # ? Синхронизация
        self.sync = QPushButton()
        self.sync.setToolTip(lang[language]['sync_but'])
        self.sync.clicked.connect(self.slot_sync)
        self.sync.setIcon(QIcon(file_sync_icon))
        self.sync.setIconSize(QSize(30, 30))
        self.sync.setFixedSize(QSize(50, 50))

        # ? Удаление
        self.delete = QPushButton()
        self.delete.setToolTip(lang[language]['delete_but'])
        self.delete.clicked.connect(self.slot_delete)
        self.delete.setIcon(QIcon(file_delete_icon))
        self.delete.setIconSize(QSize(30, 30))
        self.delete.setFixedSize(QSize(50, 50))

        # ! Разметка
        self.row = QHBoxLayout()
        self.row.setSpacing(0)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.addWidget(self.text_e, 1)
        self.row.addWidget(self.sync, 1)
        self.row.addWidget(self.delete, 1)
        self.setLayout(self.row)

    def slot_delete(self):
        if remove_local_note(self.name):
            self.itemDeleted.emit(self.__item)

    def slot_sync(self):
        self.itemSync.emit(self.__item)

    def slot_text_changed(self, new: str = ''):
        if rename_local_note(self.name, new):
            self.name = new
            self.text_e.setText('  ' + new)


class Settings(QWidget):
    def __init__(self, app, language: str = 'ru'):
        super().__init__()
        self.parent = app
        self.setFixedSize(QSize(250, 50))

        # ? Новая заметка
        self.add_note = QPushButton()
        self.add_note.setToolTip(lang[language]['add_but'])
        self.add_note.setIcon(QIcon(file_new_note_icon))
        self.add_note.setIconSize(QSize(30, 30))
        self.add_note.setMinimumSize(QSize(50, 50))

        # ? Настройки
        self.settings = QPushButton()
        self.settings.setToolTip(lang[language]['settings_but'])
        self.settings.setIcon(QIcon(file_settings_icon))
        self.settings.setIconSize(QSize(40, 40))
        self.settings.setMinimumSize(QSize(50, 50))

        # ! Разметка
        self.row = QHBoxLayout()
        self.row.setSpacing(0)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.addWidget(self.add_note, 1)
        self.row.addWidget(self.settings, 1)
        self.setLayout(self.row)
