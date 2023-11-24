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

from settings import (
    FONT_EDITOR_TEXT_SIZE,
    FONT_EDITOR_TEXT_FAMILY,
    FONT_EDITOR_TEXT_BOND,

    FONT_EDITOR_TITLE_SIZE,
    FONT_EDITOR_TITLE_FAMILY,
    FONT_EDITOR_TITLE_BOND,

    TITLE_MAX_LEN,

    EDITOR_TITLE_MAX_HEIGHT,

    SPACER_ITEM_SIZE,
)
from lang import lang
from settings import ALL_MARGINS, ALL_SPASING


class EditorUI(QWidget):
    def __init__(self, language: str, title_size: int, text_size: int) -> None:
        super().__init__()

        self.col = QVBoxLayout()
        self.col.setContentsMargins(ALL_MARGINS, ALL_MARGINS, ALL_MARGINS, ALL_MARGINS)
        self.col.setSpacing(ALL_SPASING)
        self.setLayout(self.col)

        # Название
        self.title_i = QLineEdit()
        self.title_i.setMaximumHeight(EDITOR_TITLE_MAX_HEIGHT)
        # self.title_i.setSI
        self.title_i.setFont(QFont(
            FONT_EDITOR_TITLE_FAMILY,
            title_size,
            FONT_EDITOR_TITLE_BOND
        ))
        self.title_i.setPlaceholderText(lang[language]['emp_title'])
        self.title_i.setMaxLength(TITLE_MAX_LEN)
        self.col.addWidget(self.title_i)

        # Разделитель
        self.col.addSpacerItem(
            QSpacerItem(SPACER_ITEM_SIZE[0], SPACER_ITEM_SIZE[1])
        )

        # Редактор
        self.editor_i = QTextEdit()
        self.editor_i.setFontPointSize(text_size)
        self.editor_i.setPlaceholderText(lang[language]['emp_inner'])
        self.col.addWidget(self.editor_i)

