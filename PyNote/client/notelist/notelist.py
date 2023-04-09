from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6 import QtCore


class NoteList(QWidget):
    def __init__(self):
        super().__init__()
        self.column = QVBoxLayout()
        self.setLayout(self.column)
        self.column.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.column.setSpacing(0)
        self.column.setContentsMargins(0, 0, 0, 0)
        self.setMaximumWidth(230)

    def add(self, widget):
        self.column.addWidget(widget, 1)

        # https://stackoverflow.com/questions/948444/qlistview-qlistwidget-with-custom-items-and-custom-item-widgets
