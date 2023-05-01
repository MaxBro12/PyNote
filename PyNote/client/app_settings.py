from PySide6.QtWidgets import (
    QWidget,
    QDialog,

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

from settings import (
    Config,
    Theme,
)
from language import lang


class App_Settings(QDialog):
    update_con = Signal()

    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config

        # ! Разметка
        self.l_main = QVBoxLayout()
        self.l_main.setContentsMargins(0, 0, 0, 0)
        self.l_main.setSpacing(0)
        self.setFixedSize(QSize(300, 500))

        self.as_lang = AS_lang()
        self.l_main.addLayout(self.as_lang)
        self.as_theme = AS_theme()
        self.l_main.addLayout(self.as_theme)
        self.as_opacity = AS_opacity()
        self.l_main.addLayout(self.as_opacity)
        self.as_name = AS_username()
        self.l_main.addLayout(self.as_name)
        self.as_pass = AS_password()
        self.l_main.addLayout(self.as_pass)
        self.as_key = AS_waytokey()
        self.l_main.addLayout(self.as_key)

    def update_theme(self):
        pass

    def update_config(self):
        pass


class AS_lang(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QComboBox()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_theme(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QComboBox()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_opacity(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_username(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_password(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_waytokey(QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit()
        self.addWidget(self.text)
        self.addWidget(self.box)
