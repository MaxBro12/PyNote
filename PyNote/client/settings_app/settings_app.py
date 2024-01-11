from http import server
from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QHBoxLayout,
    QListWidget,
)
from PySide6.QtCore import (
    QSize,
    QTimer,
    QThread,
)

from .settings_l_pannel import (
    SettingsGeneral,
    SettingsUser,
    SettingsServer,
)
from .server_thread import WorkerServerSt
from core import (
    read_toml,
    write_toml,
)

from lang import lang
from settings import (
    SETTINGS_APP_SIZE,
    SETTINGS_APP_L_PANNEL_SIZE,
    FILE_SETTINGS,
    TIMER_SERVER_STATUS_CALL,

    ALL_MARGINS,
    ALL_SPASING,
)
from spec_types import User


class SettingsWindow(QWidget):
    def __init__(self):
        # ! Инициализация
        super().__init__()
        self.setWindowTitle('PyNote settings')
        self.setBaseSize(QSize(SETTINGS_APP_SIZE[0], SETTINGS_APP_SIZE[1]))
        self.config = read_toml(FILE_SETTINGS)

        self.col = QHBoxLayout()
        self.col.setContentsMargins(ALL_MARGINS)
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

        # ! Dialogs
        self.settingsUser.new_user.clicked.connect(self.server_create_user)
        self.settingsUser.delete_user.clicked.connect(self.server_delete_user)


        # ! Server call
        self.server_thread = QThread()
        self.server_worker = WorkerServerSt()
        self.server_worker.moveToThread(self.server_thread)
        self.server_thread.started.connect(self.server_worker.get_server_st)

        self.timer = QTimer()
        self.timer.setInterval(TIMER_SERVER_STATUS_CALL)
        self.timer.timeout.connect(self.server_call)
        self.timer.start()

    def test_call(self, s = ''):
        print(f'Test call {s}')
    
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

    # ? Server part
    def server_call(self):
        self.server_thread.start()
        self.server_worker.get_server_st(self.config['server']['host'])
        self.settingsServer.status_i.set_color(self.server_worker.server_st)

    def server_create_user(self):
        self.server_thread.start()
        self.server_worker.create_new_user(
            self.config['server']['host'],
            User(
                self.config['server']['token'],
                self.config['user']['username'],
                self.config['user']['password']
            ),
            self.config['MAIN']['lang']
        )

    def server_delete_user(self):
        self.server_thread.start()
        self.server_worker.delete_new_user(
            self.config['server']['host'],
            User(
                self.config['server']['token'],
                self.config['user']['username'],
                self.config['user']['password']
            ),
            self.config['MAIN']['lang']
        )