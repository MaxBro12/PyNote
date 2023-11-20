from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
    QComboBox,
    QListWidget,
)
from PySide6.QtCore import (
    QSize, Qt
)

from core import (
    read_toml,
    write_toml,
    toml_type_check,
)

from lang import lang
from settings import (
    SETTINGS_APP_SIZE,
    SETTINGS_APP_L_PANNEL_SIZE,
    FILE_SETTINGS,

    ALL_MARGINS,
    ALL_SPASING,
)


class SettingsWindow(QWidget):
    def __init__(self):
        # ! Инициализация
        super().__init__()
        self.setBaseSize(QSize(SETTINGS_APP_SIZE[0], SETTINGS_APP_SIZE[1]))
        self.config = read_toml(FILE_SETTINGS)

        self.col = QHBoxLayout()
        self.col.setContentsMargins(ALL_MARGINS, ALL_MARGINS, ALL_MARGINS, ALL_MARGINS)
        self.col.setSpacing(ALL_SPASING)
        self.setLayout(self.col)

        self.left_p = QListWidget()
        self.left_p.setMaximumWidth(SETTINGS_APP_L_PANNEL_SIZE)
        self.col.addWidget(self.left_p)

        self.right_p = QStackedWidget()
        self.col.addWidget(self.right_p)

        self.settingsGeneral = SettingsGeneral(self.config)
        self.right_p.addWidget(self.settingsGeneral)
        self.settingsUser= SettingsUser(self.config)
        self.right_p.addWidget(self.settingsUser)
        self.settingsServer = SettingsServer(self.config)
        self.right_p.addWidget(self.settingsServer)

        # Установки левой панели
        self.left_p.addItem(
            lang[self.config['MAIN']['lang']]['set_gen']
        )
        self.left_p.addItem(
            lang[self.config['MAIN']['lang']]['set_user']
        )
        self.left_p.addItem(
            lang[self.config['MAIN']['lang']]['set_server']
        )
        self.right_p.setCurrentIndex(0)
        # self.left_p.itemPressed.connect(self.test_call)
        self.left_p.itemClicked.connect(self.change_st_widget)

        # Подключаем основные настройки
        self.settingsGeneral.height_i.setText(str(self.config['MAIN']['height']))
        self.settingsGeneral.height_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.width_i.setText(str(self.config['MAIN']['width']))
        self.settingsGeneral.width_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.opacity_i.setText(str(self.config['MAIN']['opacity']))
        self.settingsGeneral.opacity_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.lang_i.setCurrentText(self.config['MAIN']['lang'])
        self.settingsGeneral.lang_i.currentIndexChanged.connect(self.save_config)
        self.settingsGeneral.theme_i.setCurrentText(self.config['MAIN']['theme'])
        self.settingsGeneral.theme_i.currentIndexChanged.connect(self.save_config)
        self.settingsGeneral.font_title_i.setText(str(self.config['MAIN']['font_editor_title_size']))
        self.settingsGeneral.font_title_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.font_text_i.setText(str(self.config['MAIN']['font_editor_text_size']))
        self.settingsGeneral.font_text_i.editingFinished.connect(self.save_config) 
        self.settingsGeneral.font_nl_i.setText(str(self.config['MAIN']['font_notes_list_size']))
        self.settingsGeneral.font_nl_i.editingFinished.connect(self.save_config)

        # Подключаем раздел пользователя
        self.settingsUser.username_i.setText(self.config['user']['username'])
        self.settingsUser.username_i.editingFinished.connect(self.save_config)
        self.settingsUser.password_i.setText(self.config['user']['password'])
        self.settingsUser.password_i.editingFinished.connect(self.save_config)
        self.settingsUser.wtkey_i.setText(self.config['user']['wtkey'])
        self.settingsUser.wtkey_i.editingFinished.connect(self.save_config)

        # Подключаем раздел сервера 
        self.settingsServer.host_i.setText(self.config['server']['host'])
        self.settingsServer.host_i.editingFinished.connect(self.save_config)
        self.settingsServer.token_i.setText(self.config['server']['token'])
        self.settingsServer.token_i.editingFinished.connect(self.save_config)

    def test_call(self, s = ''):
        print('YES!', s)
    
    def change_st_widget(self):
        self.right_p.setCurrentIndex(self.left_p.currentRow())

    def load_config(self):
        self.config = read_toml(FILE_SETTINGS)

    def save_config(self):
        self.config['MAIN']['width'] = int(self.settingsGeneral.width_i.text())
        self.config['MAIN']['height'] = int(self.settingsGeneral.height_i.text())
        self.config['MAIN']['opacity'] = float(self.settingsGeneral.opacity_i.text())
        self.config['MAIN']['lang'] = str(self.settingsGeneral.lang_i.currentText())
        self.config['MAIN']['theme'] = str(self.settingsGeneral.theme_i.currentText())
        self.config['MAIN']['font_editor_title_size'] = int(self.settingsGeneral.font_title_i.text())
        self.config['MAIN']['font_editor_text_size'] = int(self.settingsGeneral.font_text_i.text())
        self.config['MAIN']['font_notes_list_size'] = int(self.settingsGeneral.font_nl_i.text())

        self.config['user']['username'] = str(self.settingsUser.username_i.text())
        self.config['user']['password'] = str(self.settingsUser.password_i.text())
        self.config['user']['wtkey'] = str(self.settingsUser.wtkey_i.text())

        self.config['server']['host'] = str(self.settingsServer.host_i.text())
        self.config['server']['token'] = str(self.settingsServer.token_i.text())

        write_toml(self.config, FILE_SETTINGS)


class SettingsMainPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.row = QGridLayout()
        self.row.setSpacing(ALL_SPASING)
        self.row.setContentsMargins(2, ALL_MARGINS, ALL_MARGINS, ALL_MARGINS)
        self.row.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.row)


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

