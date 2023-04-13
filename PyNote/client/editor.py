from PySide6.QtWidgets import (
    QVBoxLayout,

    QLineEdit,
    QTextEdit,

    QWidget,
)


class Editor(QVBoxLayout):
    def __init__(self, title: str = '', inner: str = ''):
        # ! Основа
        super().__init__()

        # ? Редактор названия
        self.title_editor = QTextEdit()
        self.title_editor.setText(title)
        self.title_editor.setMaximumHeight(30)
        self.title_editor.setMinimumHeight(30)

        # ? Редактор текста
        self.text_editor = QTextEdit()
        self.text_editor.setText(inner)

        # ? Добавляем все в лайаут
        self.addWidget(self.title_editor)
        self.addWidget(self.text_editor)

    def update_info(self, title: str = '', inner: str = ''):
        self.title_editor.setText(title)
        self.text_editor.setText(inner)
