from PySide6 import QtCore, QtWidgets, QtGui


class MyApp(QtWidgets.QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config

        # self.setWindowIcon(QtGui.QIcon('appico.ico'))
        self.setWindowTitle('PyNote')

        # Размеры
        self.resize(1000, 700)
        # self.setFixedSize()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
