from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
)
from .settings_main_pannel import SettingsMainPanel

from lang import lang


class SettingsUser(SettingsMainPanel):
    def __init__(self, conf):
        super().__init__()

        self.conf = conf

        # username
        self.username_l = QLabel()
        self.username_l.setText(
            lang[conf['MAIN']['lang']]['set_username_l']
        )

        self.username_i = QLineEdit()
        self.username_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_username_i']
        )
        # password
        self.password_l = QLabel()
        self.password_l.setText(
            lang[conf['MAIN']['lang']]['set_password_l']
        )

        self.password_i = QLineEdit()
        self.password_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_password_i']
        )

        # wtkey
        self.wtkey_l = QLabel()
        self.wtkey_l.setText(
            lang[conf['MAIN']['lang']]['set_wtkey_l']
        )

        self.wtkey_i = QLineEdit()
        self.wtkey_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_wtkey_i']
        )

        self.row.addWidget(self.username_l, 0, 0)
        self.row.addWidget(self.username_i, 0, 1)
        self.row.addWidget(self.password_l, 1, 0)
        self.row.addWidget(self.password_i, 1, 1)
        self.row.addWidget(self.wtkey_l, 2, 0)
        self.row.addWidget(self.wtkey_i, 2, 1)


