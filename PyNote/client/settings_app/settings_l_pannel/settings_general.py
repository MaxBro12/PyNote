from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QComboBox,
)
from .settings_main_pannel import SettingsMainPanel

from lang import lang


class SettingsGeneral(SettingsMainPanel):
    def __init__(self, conf):
        super().__init__()

        self.conf = conf

        # width
        self.width_l = QLabel()
        self.width_l.setText(
            lang[conf['MAIN']['lang']]['set_wid_l']
        )

        self.width_i = QLineEdit()
        self.width_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_wid_i']
        )

        # height
        self.height_l = QLabel()
        self.height_l.setText(
            lang[conf['MAIN']['lang']]['set_hei_l']
        )

        self.height_i = QLineEdit()
        self.height_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_hei_i']
        )

        # opacity
        self.opacity_l = QLabel()
        self.opacity_l.setText(
            lang[conf['MAIN']['lang']]['set_opa_l']
        )

        self.opacity_i = QLineEdit()
        self.opacity_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['set_opa_i']
        )

        # lang
        self.lang_l = QLabel()
        self.lang_l.setText(
            lang[conf['MAIN']['lang']]['set_lang_l']
        )

        self.lang_i = QComboBox()
        self.lang_i.addItems(list(lang.keys()))

        # tmeme
        self.theme_l = QLabel()
        self.theme_l.setText(
            lang[conf['MAIN']['lang']]['set_theme_l']
        )

        self.theme_i = QComboBox()

        # title_size
        self.font_title_l = QLabel()
        self.font_title_l.setText(
            lang[conf['MAIN']['lang']]['set_title_l']
        )
        self.font_title_i = QLineEdit()

        # font_text
        self.font_text_l = QLabel()
        self.font_text_l.setText(
            lang[conf['MAIN']['lang']]['set_text_l']
        )
        self.font_text_i = QLineEdit()

        # font_text
        self.font_nl_l = QLabel()
        self.font_nl_l.setText(
            lang[conf['MAIN']['lang']]['set_nl_l']
        )
        self.font_nl_i = QLineEdit()

        # ! Добавляем к лойауту
        self.row.addWidget(self.width_l, 0, 0)
        self.row.addWidget(self.width_i, 0, 1)
        self.row.addWidget(self.height_l, 1, 0)
        self.row.addWidget(self.height_i, 1, 1)
        self.row.addWidget(self.opacity_l, 2, 0)
        self.row.addWidget(self.opacity_i, 2, 1)
        self.row.addWidget(self.lang_l, 3, 0)
        self.row.addWidget(self.lang_i, 3, 1)
        self.row.addWidget(self.theme_l, 4, 0)
        self.row.addWidget(self.theme_i, 4, 1)
        self.row.addWidget(self.font_title_l, 5, 0)
        self.row.addWidget(self.font_title_i, 5, 1)
        self.row.addWidget(self.font_text_l, 6, 0)
        self.row.addWidget(self.font_text_i, 6, 1)
        self.row.addWidget(self.font_nl_l, 7, 0)
        self.row.addWidget(self.font_nl_i, 7, 1)


