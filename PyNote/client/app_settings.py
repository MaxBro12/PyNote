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

from settings import (
    Config,
    Theme,
)
from language import lang


class App_Settings(QWidget):
    update_con = Signal()

    def __init__(self, config: Config) -> None:
        super().__init__()
        self.config = config

        # ! Разметка
        self.l_main = QVBoxLayout()
        self.l_main.setContentsMargins(0, 0, 0, 0)
        self.l_main.setSpacing(0)
        self.setFixedSize(QSize(300, 500))

    def update_theme(self):
        pass

    def update_config(self):
        pass


class AS_lang(QHBoxLayout):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel(text)
        self.box = QComboBox()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_theme(QHBoxLayout):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel(text)
        self.box = QComboBox()
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_opacity(QHBoxLayout):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit(text)
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_username(QHBoxLayout):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit(text)
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_password(QHBoxLayout):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit(text)
        self.addWidget(self.text)
        self.addWidget(self.box)


class AS_waytokey(QHBoxLayout):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        self.text = QLabel()
        self.box = QLineEdit(text)
        self.addWidget(self.text)
        self.addWidget(self.box)
