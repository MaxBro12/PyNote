from PySide6.QtWidgets import (
    QVBoxLayout,

    QLineEdit,
    QTextEdit,
    QPlainTextEdit,

    QListWidgetItem,
    QWidget,

    QSpacerItem,
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QFont


from core import create_log_file
from handlers import (
    rename_local_note,
    save_local_note,
)

from settings import (
    title_max_length,

    font_editor_title_family,
    font_editor_title_size,

    font_editor_text_family,
    font_editor_text_size,
)
from language import lang


class Editor(QVBoxLayout):
    newNote = Signal(str)

    def __init__(self, language: str = 'ru'):
        # ! Основа
        super().__init__()
        self.save_times = 0
        self.widget_i = None

        # ? Редактор названия
        self.title_e = QLineEdit()
        self.title_e.setFont(QFont(
            font_editor_title_family,
            font_editor_title_size,
            99
        ))
        self.title_e.setPlaceholderText(lang[language]['emp_title'])
        self.title_e.editingFinished.connect(self.slot_rename_note)
        self.title_e.setFixedHeight(30)
        self.title_e.setTextMargins(2, 3, 0, 0)
        self.title_e.setMaxLength(title_max_length)

        # ? Редактор текста
        self.text_e = QTextEdit()
        self.text_e.setPlaceholderText(lang[language]['emp_inner'])
        self.text_e.textChanged.connect(self.slot_save_note)

        # ? Добавляем все в лайаут
        self.addWidget(self.title_e, 1)
        self.addSpacerItem(QSpacerItem(30, 5))
        self.addWidget(self.text_e, 0)

    def update_info(self, widget):
        self.widget_i = widget
        self.title_e.setText(self.widget_i.name)
        self.text_e.setPlainText(self.widget_i.inner)

    def slot_save_note(self):
        if self.widget_i is None:
            create_log_file(
                f'Виджет не был присвоен: {self.title_e.text()}',
                'error'
            )
        else:
            # ! Локальное сохранение изменений
            if save_local_note(
                self.title_e.text(),
                self.text_e.toPlainText()
            ):
                self.widget_i.inner = self.text_e.toPlainText()
                self.save_times += 1

        # ! Выгрузка на сервак
        pass

    def slot_rename_note(self):
        if self.widget_i is None:
            print('yees')
            self.newNote.emit(self.title_e.text())

        if self.widget_i is not None:
            self.widget_i.slot_text_changed(self.title_e.text())

    def slot_call_new_note(self, widget):
        self.widget_i = widget
