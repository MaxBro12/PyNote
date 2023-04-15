from PySide6.QtWidgets import (
    QVBoxLayout,

    QLineEdit,
    QTextEdit,
    QPlainTextEdit,

    QListWidgetItem,
    QWidget,
)
from PySide6.QtCore import Signal


from handlers import (
    rename_local_note,
    save_local_note,
)

from settings import (
    server_upload_note_after_changes,
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
        self.title_e.setPlaceholderText(lang[language]['emp_title'])
        self.title_e.editingFinished.connect(self.slot_rename_note)
        self.title_e.setFixedHeight(30)
        self.title_e.setTextMargins(2, 0, 0, 0)
        self.title_e.setMaxLength(20)

        # ? Редактор текста
        self.text_e = QTextEdit()
        self.text_e.setPlaceholderText(lang[language]['emp_inner'])
        self.text_e.textChanged.connect(self.slot_save_note)
        # self.text_e.setText(widget.inner)
        # self.text_e.setTextMargins(5, 0, 0, 0)

        # ? Добавляем все в лайаут
        self.addWidget(self.title_e, 1)
        self.addWidget(self.text_e, 0)

    def update_info(self, widget):
        self.widget_i = widget
        self.title_e.setText(self.widget_i.name)
        self.text_e.setPlainText(self.widget_i.inner)

    def slot_save_note(self):
        if self.widget_i is None:
            print("WTF?????")
        else:
            # ! Локальное сохранение изменений
            if save_local_note(
                self.title_e.text(),
                self.text_e.toPlainText()
            ):
                self.widget_i.inner = self.text_e.toPlainText()
                self.save_times += 1

        # ! Выгрузка на сервак
        if self.save_times >= server_upload_note_after_changes:
            pass

    def slot_rename_note(self):
        if self.widget_i is None:
            print('yees')
            self.newNote.emit(self.title_e.text())

        if self.widget_i is not None:
            self.widget_i.slot_text_changed(self.title_e.text())

    def slot_call_new_note(self, widget):
        self.widget_i = widget
