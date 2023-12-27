from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QWidget,
)
from PySide6.QtCore import QSize
from PySide6.QtGui import QPalette, QColor, Qt
from .settings_main_pannel import SettingsMainPanel

from lang import lang


class SettingsServer(SettingsMainPanel):
    def __init__(self, conf):
        super().__init__()

        self.conf = conf

        # host
        self.host_l = QLabel()
        self.host_l.setText(
            lang[conf['MAIN']['lang']]['set_host_l']
        )

        self.host_i = QLineEdit()
        self.host_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_host_i']
        )

        # Mark
        self.status_l = QLabel()
        self.status_l.setText(
            lang[conf['MAIN']['lang']]['serv_st_l']
        )

        self.status_i = Color('red')
        # self.status_l.setPlaceholderText(
        #     lang[conf['MAIN']['lang']]['serv_st_i']
        # )

        # token
        self.token_l = QLabel()
        self.token_l.setText(
            lang[conf['MAIN']['lang']]['set_token_l']
        )

        self.token_i = QLineEdit()
        self.token_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_token_i']
        )

        self.row.addWidget(self.host_l, 0, 0)
        self.row.addWidget(self.host_i, 0, 1)
        self.row.addWidget(self.status_l, 1, 0)
        self.row.addWidget(self.status_i, 1, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
        self.row.addWidget(self.token_l, 2, 0)
        self.row.addWidget(self.token_i, 2, 1)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setFixedSize(QSize(10, 10))
        self.setAutoFillBackground(True)
        self.set_color()

    def set_color(self, st: bool = False):
        if st is False:
            color = 'red'
        else:
            color = 'green'
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
