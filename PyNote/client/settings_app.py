from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
    QComboBox,
    QPushButton,
    QListWidget,
)
from PySide6.QtCore import (
    QSize,
    Signal,
)

from core import (
    read_toml,
    write_toml,
    toml_type_check,
    get_profiles_names,
)

from lang import lang
from settings import (
    SETTINGS_APP_SIZE,
    SETTINGS_APP_L_PANNEL_SIZE,
    FILE_SETTINGS,

    SETTINGS_GENERAL,
    SETTINGS_ML,
    SETTINGS_MARKET,

    ALL_MARGINS,
    ALL_SPASING,
)


class SettingsWindow(QWidget):
    def __init__(self):
        # ! Инициализация
        super().__init__()
        self.setBaseSize(QSize(SETTINGS_APP_SIZE[0], SETTINGS_APP_SIZE[1]))
        self.config = read_toml(FILE_SETTINGS)
        if self.config['MAIN']['use_self_window']:
            pass

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
        self.settingsML = SettingsMiningLedger()
        self.right_p.addWidget(self.settingsML)
        self.settingsMarket = SettingsMarket()
        self.right_p.addWidget(self.settingsMarket)

        # Установки левой панели
        self.left_p.addItem(
            lang[self.config['MAIN']['lang']]['main']['set_main']
        )
        self.left_p.addItem(
            lang[self.config['MAIN']['lang']]['main']['set_mining']
        )
        self.left_p.addItem(
            lang[self.config['MAIN']['lang']]['main']['set_market']
        )
        self.right_p.setCurrentIndex(0)
        # self.left_p.itemPressed.connect(self.test_call)
        self.left_p.itemClicked.connect(self.change_st_widget)

        # MAIN
        self.settingsGeneral.height_i.setText(str(self.config['MAIN']['height']))
        self.settingsGeneral.height_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.width_i.setText(str(self.config['MAIN']['width']))
        self.settingsGeneral.width_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.opacity_i.setText(str(self.config['MAIN']['opacity']))
        self.settingsGeneral.opacity_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.lang_i.setCurrentText(self.config['MAIN']['lang'])
        self.settingsGeneral.lang_i.currentIndexChanged.connect(self.save_config)
        self.settingsGeneral.resizeable_i.setChecked(self.config['MAIN']['resizeable'])
        self.settingsGeneral.resizeable_i.stateChanged.connect(self.save_config)
        self.settingsGeneral.always_on_i.setChecked(self.config['MAIN']['always_on'])
        self.settingsGeneral.always_on_i.stateChanged.connect(self.save_config)
        self.settingsGeneral.usw_i.setChecked(self.config['MAIN']['use_self_window'])
        self.settingsGeneral.usw_i.stateChanged.connect(self.save_config)
        self.settingsGeneral.elf_i.setText(str(self.config['MAIN']['eve_logs_folder']))
        self.settingsGeneral.elf_i.editingFinished.connect(self.save_config)
        self.settingsGeneral.last_pr_i.setCurrentText(self.config['MAIN']['last_profile'])
        self.settingsGeneral.last_pr_i.currentIndexChanged.connect(self.save_config)

    def test_call(self, s = ''):
        print('YES!', s)
    
    def change_st_widget(self):
        self.right_p.setCurrentIndex(self.left_p.currentRow())

    def load_config(self):
        self.config = read_toml(FILE_SETTINGS)

    def save_config(self):
        print('Config saved')
        self.config['MAIN']['width'] = int(self.settingsGeneral.width_i.text())
        self.config['MAIN']['height'] = int(self.settingsGeneral.height_i.text())
        self.config['MAIN']['opacity'] = float(self.settingsGeneral.opacity_i.text())
        self.config['MAIN']['lang'] = str(self.settingsGeneral.lang_i.currentText())
        self.config['MAIN']['resizeable'] = bool(self.settingsGeneral.resizeable_i.isChecked())
        self.config['MAIN']['always_on'] = bool(self.settingsGeneral.always_on_i.isChecked())
        self.config['MAIN']['use_self_window'] = bool(self.settingsGeneral.usw_i.isChecked())
        self.config['MAIN']['eve_logs_folder'] = str(self.settingsGeneral.elf_i.text())
        self.config['MAIN']['last_profile'] = str(self.settingsGeneral.last_pr_i.currentText())
        write_toml(self.config, FILE_SETTINGS)


class SettingsMainPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.row = QGridLayout()
        self.row.setSpacing(ALL_SPASING)
        self.row.setContentsMargins(2, ALL_MARGINS, ALL_MARGINS, ALL_MARGINS)
        self.setLayout(self.row)


class SettingsGeneral(SettingsMainPanel):
    def __init__(self, conf):
        super().__init__()

        self.conf = conf

        # width
        self.width_l = QLabel()
        self.width_l.setText(
            lang[conf['MAIN']['lang']]['settings']['width_l']
        )

        self.width_i = QLineEdit()
        self.width_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['settings']['width_i']
        )

        # height
        self.height_l = QLabel()
        self.height_l.setText(
            lang[conf['MAIN']['lang']]['settings']['height_l']
        )

        self.height_i = QLineEdit()
        self.height_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['settings']['height_i']
        )

        # opacity
        self.opacity_l = QLabel()
        self.opacity_l.setText(
            lang[conf['MAIN']['lang']]['settings']['opacity_l']
        )

        self.opacity_i = QLineEdit()
        self.opacity_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['settings']['opacity_i']
        )

        # lang
        self.lang_l = QLabel()
        self.lang_l.setText(
            lang[conf['MAIN']['lang']]['settings']['lang_l']
        )

        self.lang_i = QComboBox()
        self.lang_i.addItems(list(lang.keys()))

        # resizeable
        self.resizeable_l = QLabel()
        self.resizeable_l.setText(
            lang[conf['MAIN']['lang']]['settings']['resizeable_l']
        )

        self.resizeable_i = QCheckBox()

        # always_on
        self.always_on_l = QLabel()
        self.always_on_l.setText(
            lang[conf['MAIN']['lang']]['settings']['always_on_l']
        )

        self.always_on_i = QCheckBox()

        # use_self_win
        self.usw_l = QLabel()
        self.usw_l.setText(
            lang[conf['MAIN']['lang']]['settings']['usw_l']
        )

        self.usw_i = QCheckBox()

        # use_self_win
        self.elf_l = QLabel()
        self.elf_l.setText(
            lang[conf['MAIN']['lang']]['settings']['elf_l']
        )

        self.elf_i = QLineEdit()
        self.elf_i.setPlaceholderText(
            lang[conf['MAIN']['lang']]['settings']['elf_i']
        )

        # last profile
        self.last_pr_l = QLabel()
        self.last_pr_l.setText(
            lang[conf['MAIN']['lang']]['settings']['last_pr_l']
        )

        self.last_pr_i = QComboBox()
        self.last_pr_i.addItems(list(get_profiles_names()))

        # ! Добавляем к лойауту
        self.row.addWidget(self.width_l, 0, 0)
        self.row.addWidget(self.width_i, 0, 1)
        self.row.addWidget(self.height_l, 1, 0)
        self.row.addWidget(self.height_i, 1, 1)
        self.row.addWidget(self.opacity_l, 2, 0)
        self.row.addWidget(self.opacity_i, 2, 1)
        self.row.addWidget(self.lang_l, 3, 0)
        self.row.addWidget(self.lang_i, 3, 1)
        self.row.addWidget(self.resizeable_l, 4, 0)
        self.row.addWidget(self.resizeable_i, 4, 1)
        self.row.addWidget(self.always_on_l, 5, 0)
        self.row.addWidget(self.always_on_i, 5, 1)
        self.row.addWidget(self.usw_l, 6, 0)
        self.row.addWidget(self.usw_i, 6, 1)
        self.row.addWidget(self.elf_l, 7, 0)
        self.row.addWidget(self.elf_i, 7, 1)
        self.row.addWidget(self.last_pr_l, 8, 0)
        self.row.addWidget(self.last_pr_i, 8, 1)


class SettingsMiningLedger(SettingsMainPanel):
    def __init__(self):
        super().__init__()

        # max_scans
        self.width_l = QLabel()

        self.width_i = QLineEdit()


class SettingsMarket(SettingsMainPanel):
    def __init__(self):
        super().__init__()

        # max_scans
        self.width_l = QLabel()

        self.width_i = QLineEdit()

