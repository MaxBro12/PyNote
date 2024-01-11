from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Qt
from settings import ALL_MARGINS, ALL_SPASING



class SettingsMainPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.row = QGridLayout()
        self.row.setSpacing(ALL_SPASING)
        self.row.setContentsMargins(ALL_MARGINS)
        self.row.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.row)

