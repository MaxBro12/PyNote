from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
)
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
        self.row.addWidget(self.token_l, 1, 0)
        self.row.addWidget(self.token_i, 1, 1)

