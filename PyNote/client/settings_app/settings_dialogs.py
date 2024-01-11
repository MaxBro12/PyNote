from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QDialogButtonBox,
    QMessageBox
)

from lang import lang
from settings import SETTINGS_DIA_SIZE


class NewUserExistsWarning(QDialog):
    def __init__(self, parent=None, language: str = 'ru') -> None:
        super().__init__(parent)
        self.setFixedSize(SETTINGS_DIA_SIZE)
        self.setWindowTitle('PyNote')

        self.col = QVBoxLayout()
        self.setLayout(self.col)

        self.label = QLabel()
        self.label.setText(lang[language]['dia_new_user_exists'])
        self.col.addWidget(self.label)

        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.col.addWidget(self.buttonBox)


class NewUserCreated(QDialog):
    def __init__(self, parent=None, language: str = 'ru', username: str = '') -> None:
        super().__init__(parent)
        self.setFixedSize(SETTINGS_DIA_SIZE)
        self.setWindowTitle('PyNote')

        self.col = QVBoxLayout()
        self.setLayout(self.col)

        self.label = QLabel()
        self.label.setText(lang[language]['dia_new_user_created'].format(username=username))
        self.col.addWidget(self.label)

        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.col.addWidget(self.buttonBox)



class UserDeleteWarning(QDialog):
    def __init__(self, parent=None, language: str = 'ru') -> None:
        super().__init__(parent)
        self.setFixedSize(SETTINGS_DIA_SIZE)
        self.setWindowTitle('PyNote')

        self.col = QVBoxLayout()
        self.setLayout(self.col)

        self.label = QLabel()
        self.label.setText(lang[language]['dia_delete_user_acces'])
        self.col.addWidget(self.label)

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.col.addWidget(self.buttonBox)


class UserWasDeletedWarning(QDialog):
    def __init__(self, parent=None, language: str = 'ru', username: str = '') -> None:
        super().__init__(parent)
        self.setFixedSize(SETTINGS_DIA_SIZE)
        self.setWindowTitle('PyNote')

        self.col = QVBoxLayout()
        self.setLayout(self.col)

        self.label = QLabel()
        self.label.setText(lang[language]['dia_user_was_deleted'].format(username=username))
        self.col.addWidget(self.label)

        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.col.addWidget(self.buttonBox)