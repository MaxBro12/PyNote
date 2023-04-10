from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6 import QtCore


from .noteitem import EmptyNote


class NoteList(QWidget):
    def __init__(self):
        super().__init__()
        self.__notes = []
        # ! Разметка
        self.column = QVBoxLayout()
        self.setLayout(self.column)
        self.column.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.column.setSpacing(5)
        self.column.setContentsMargins(0, 0, 0, 0)
        self.setFixedWidth(250)

        self.empty = EmptyNote()

    def update_list(self):
        # ? Очищаем список
        for i in range(self.column.count()):
            self.column.removeItem(self.column.itemAt(i))

        # ? Закидывем новые виджеты
        for note in self.__notes:
            self.column.addWidget(note, 0)
        self.column.addWidget(self.empty)

    def add(self, widget: QWidget):
        self.__notes.append(widget)
        self.update_list()

    @property
    def notes(self) -> list:
        return self.__notes

    def __getitem__(self, index: int) -> QWidget:
        return self.__notes[index]

    def __setitem__(self, index: int, widget: QWidget):
        self.__notes[index] = widget

    def __len__(self) -> int:
        return self.column.count()

        # https://stackoverflow.com/questions/948444/qlistview-qlistwidget-with-custom-items-and-custom-item-widgets
