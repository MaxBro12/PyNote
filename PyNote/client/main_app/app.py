from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon

from .app_ui import MainAppUI
from ..settings_app import SettingsWindow
from ..warning_app import WarningApp 
from core import (
    create_log,

    pjoin,
    wayfinder,

    read_toml,
    write_toml,
    toml_type_check,
)

from settings import (
    DIR_THEMES,
    FILE_SETTINGS,
    FILE_APP_ICON,
)


class MyAppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка конфига
        self.config = read_toml(FILE_SETTINGS) 
        
        # Доп окна
        self.warning = None
        self.settings = None
        
        # Рамка
        self.setWindowIcon(QIcon(FILE_APP_ICON))
        self.setWindowTitle('PyNote')

        # ? Размеры
        self.resize(self.config['app']['width'], self.config['app']['height'])
        self.setMinimumSize(300, 400)
                
        # Тема
        self.load_theme()

    # MAIN ====================================================================
    def show_settings(self):
        if self.settings is None:
            self.settings = SettingsWindow()
            create_log('Show settings', 'debug')
            self.settings.show()
        else:
            self.settings = None

    def show_warning(self, msg: str):
        if self.warning is None:
            self.warning = WarningApp(msg)
            create_log(f'Show Warning:\n{msg}', 'debug')
            self.warning.show()
        else:
            self.warning = None

    def load_config(self):
        self.config = read_toml(FILE_SETTINGS)

    def load_theme(self):
        # Проверяем если значение вообще не пустное
        if self.config['MAIN']['theme']:
            way = pjoin(DIR_THEMES, self.config['MAIN']['theme'])
            # Проверяем существование файла до открытия
            if wayfinder(way):
                with open(way) as f:
                    self.setStyleSheet(f.read())

