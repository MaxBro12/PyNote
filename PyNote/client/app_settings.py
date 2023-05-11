from PySide6.QtWidgets import (
    QWidget,

    QLabel,
    QComboBox,
    QLineEdit,

    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtCore import (
    QSize,
    Signal,
)
from PySide6.QtGui import QIcon

from core import read, pjoin

from settings import (
    file_icon,
    fold_themes,
)
from spec_types import (
    Config,
    Theme,

    cast
)
from language import lang


class App_Settings(QWidget):
    update_conf = Signal()

    def __init__(self, config: Config, theme: Theme) -> None:
        super().__init__()
        self.config = config
        self.theme = theme

        self.setWindowIcon(QIcon(file_icon))
        self.setWindowTitle('PyNote')

        self.resize(400, 500)
        self.setMinimumSize(250, 350)

        # ! Разметка
        self.l_main = QVBoxLayout()
        self.l_main.setContentsMargins(5, 5, 5, 5)
        # self.l_main.setSpacing(0)
        # self.setFixedSize(QSize(300, 500))

        self.as_lang = AS_lang(self, config)
        self.l_main.addWidget(self.as_lang)
        self.as_theme = AS_theme()
        self.l_main.addWidget(self.as_theme)
        self.as_opacity = AS_opacity()
        self.l_main.addWidget(self.as_opacity)
        self.as_name = AS_username()
        self.l_main.addWidget(self.as_name)
        self.as_pass = AS_password()
        self.l_main.addWidget(self.as_pass)
        self.as_key = AS_waytokey()
        self.l_main.addWidget(self.as_key)

        self.setLayout(self.l_main)

        # ! Доп действия
        self.update_theme()

    def update_theme(self):
        self.theme = cast(
            Theme, read(pjoin(fold_themes, self.config['app']['theme']))
        )
        self.setStyleSheet(
            f"background-color: {self.theme['background']};" +
            f"color: {self.theme['text_color']};" +
            # f"border-color: {theme['background']};" +
            f"border-style: outset;"
        )

    def update_config(self):
        pass


class AS_lang(QWidget):
    def __init__(self, parent, conf: Config) -> None:
        super().__init__(parent)
        self.setStyleSheet(
            f"background-color: {parent.theme['side_panel']};" +
            "border-radius: 20px;"
        )

        # ! Текст
        self.text = QLabel()
        self.text.setText(lang[conf['app']['lang']]['as_lang'])

        # ! Выбор
        self.box = QComboBox()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.setLayout(self.row)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)


class AS_theme(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text = QLabel()
        self.box = QComboBox()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)


class AS_opacity(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text = QLabel()
        self.box = QComboBox()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)


class AS_username(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text = QLabel()
        self.box = QComboBox()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)


class AS_password(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text = QLabel()
        self.box = QComboBox()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)


class AS_waytokey(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.text = QLabel()
        self.box = QComboBox()

        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)
