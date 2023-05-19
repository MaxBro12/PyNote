from typing import Optional
from PySide6.QtWidgets import (
    QWidget,

    QLabel,
    QComboBox,
    QLineEdit,

    QVBoxLayout,
    QHBoxLayout,

    QSizePolicy,
)
from PySide6.QtCore import (
    QSize,
    Signal,
)
from PySide6.QtGui import QIcon


from core import read, pjoin, get_files


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
        self.setMinimumSize(QSize(300, 200))
        self.setMaximumSize(QSize(350, 400))

        # ! Разметка
        self.l_main = QVBoxLayout()
        self.l_main.setContentsMargins(5, 5, 5, 5)
        # self.l_main.setSpacing(0)
        # self.setFixedSize(QSize(300, 500))

        self.as_lang = AS_lang(self, theme, config)
        self.as_lang.box.currentTextChanged.connect(self.update_config())
        self.l_main.addWidget(self.as_lang)

        self.as_theme = AS_theme(self, theme, config)
        self.as_theme.box.currentTextChanged.connect(self.update_config())
        self.l_main.addWidget(self.as_theme)

        self.as_opacity = AS_opacity(self, theme, config)
        self.as_opacity.box.editingFinished.connect(self.update_config())
        self.l_main.addWidget(self.as_opacity)

        self.as_name = AS_username(self, theme, config)
        self.as_name.box.editingFinished.connect(self.update_config())
        self.l_main.addWidget(self.as_name)

        self.as_pass = AS_password(self, theme, config)
        self.as_pass.box.editingFinished.connect(self.update_config())
        self.l_main.addWidget(self.as_pass)

        # self.as_key = AS_waytokey(self, theme, config)
        # self.l_main.addWidget(self.as_key)

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
        print('Calling update method')
        self.update_conf.emit()


class Row_Box(QWidget):
    def __init__(self, parent, theme: Theme) -> None:
        super().__init__(parent)
        self.theme = theme
        self.setMaximumHeight(50)

        # ! Холдер для текста
        self.text = QLabel()
        self.text.setFixedWidth(130)
        # ! Холдер для объекта
        self.box = QComboBox()
        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.setLayout(self.row)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)

        self.update_theme()

    def update_theme(self):
        self.setStyleSheet(
            f"""background-color: {self.theme['side_panel']};
            color: {self.theme['text_color']};
            """
        )
        self.text.setStyleSheet(
            f"""padding-left: 10px;
            border-top-left-radius: 10%;
            border-bottom-left-radius: 10%;
            """
        )
        self.box.setStyleSheet(
            """
            QComboBox {
                border: 1px solid""" + f" {self.theme['text_color']}" + """;

                border-top-right-radius: 10%;
                border-bottom-right-radius: 10%;

                padding-top: 100%;
                padding-bottom: 100%;
                padding-left: 10px;
            }
            QComboBox::on {
                padding: 0px, 0px, 0px, 0px;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox::drop-arrow {
                image: url(:/icons/expand.svg);
                width: 12px;
                height: 12px;
                margine-right: 20px;
            }
            QListView {
                border: 1px solid white;
                margin: 0px;
                padding: 0px;
                outline: 0px;
            }
            """
            # """
            # box QListView {
            #     border: 1px solid white;
            #     padding: 0, 0, 0, 0;
            # }
            # f"""border-color: {self.theme['text_color']}; border: 1px solid {self.theme['text_color']};"""
        )

    @property
    def get(self):
        return str(self.box.currentText())


class Row_Edit(QWidget):
    def __init__(self, parent, theme: Theme) -> None:
        super().__init__(parent)
        self.theme = theme
        self.setMaximumHeight(50)

        # ! Холдер для текста
        self.text = QLabel()
        self.text.setFixedWidth(130)
        # ! Холдер для объекта
        self.box = QLineEdit()
        # ? Разметка
        self.row = QHBoxLayout()
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setSpacing(0)
        self.setLayout(self.row)
        self.row.addWidget(self.text)
        self.row.addWidget(self.box)

        self.update_theme()

    def update_theme(self):
        self.setStyleSheet(
            f"""background-color: {self.theme['side_panel']};
            color: {self.theme['text_color']};
            """
        )
        self.text.setStyleSheet(
            f"""padding-left: 10px;
            border-top-left-radius: 10%;
            border-bottom-left-radius: 10%;
            """
        )
        self.box.setStyleSheet(
            f"""border-color: {self.theme['text_color']};
            border: 1px solid {self.theme['text_color']};
            padding-top: 100%;
            padding-bottom: 100%;
            padding-left: 10px;
            border-top-right-radius: 10%;
            border-bottom-right-radius: 10%;
            """
        )

    @property
    def get(self):
        return str(self.box.text())


class AS_lang(Row_Box):
    def __init__(self, parent, theme: Theme, conf: Config) -> None:
        super().__init__(parent, theme)
        # ! Текст
        self.text.setText(lang[conf['app']['lang']]['as_lang'])

        # ! Выбор
        for la in lang.keys():
            self.box.addItem(la)
        self.box.setCurrentText(conf['app']['lang'])


class AS_theme(Row_Box):
    def __init__(self, parent, theme: Theme, conf: Config) -> None:
        super().__init__(parent, theme)
        # ! Текст
        self.text.setText(lang[conf['app']['lang']]['as_theme'])

        # ! Выбор
        themes = get_files(fold_themes)
        themes = list(map(lambda x: '.'.join(x.split('.')[:-1]), themes))
        for th in themes:
            self.box.addItem(th)
        self.box.setCurrentText(conf['app']['theme'])


class AS_opacity(Row_Edit):
    def __init__(self, parent, theme: Theme, conf: Config) -> None:
        super().__init__(parent, theme)
        # ! Текст
        self.text.setText(lang[conf['app']['lang']]['as_opacity'])

        # ! Выбор
        self.box.setPlaceholderText("0.0 - 1")
        self.box.setText(str(conf['app']['opacity']))


class AS_username(Row_Edit):
    def __init__(self, parent, theme: Theme, conf: Config) -> None:
        super().__init__(parent, theme)
        # ! Текст
        self.text.setText(lang[conf['app']['lang']]['as_username'])

        # ! Выбор
        self.box.setPlaceholderText("username")
        self.box.setText(conf['user']['username'])


class AS_password(Row_Edit):
    def __init__(self, parent, theme: Theme, conf: Config) -> None:
        super().__init__(parent, theme)
        # ! Текст
        self.text.setText(lang[conf['app']['lang']]['as_password'])

        # ! Выбор
        self.box.setPlaceholderText("******")
        self.box.setText(conf['user']['password'])
