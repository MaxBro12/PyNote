from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
)
from PySide6.QtCore import QSize


from .noteitem import NoteItem, Settings


from handlers import (
    add_local_note,
    get_local_notes,
)


class NoteList(QVBoxLayout):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # ! Список:
        self.list = QListWidget()
        self.list.setMaximumWidth(250)

        # ! Настройки
        self.settings = Settings(app)

        self.addWidget(self.list, 0)
        self.addWidget(self.settings, 1)

    def add(self, name: str):
        # ? Создаем ячейку
        item = QListWidgetItem(self.list)
        item.setSizeHint(QSize(250, 50))

        # ? Создаем заметку
        note_name = f'New-{len(get_local_notes())}'
        add_local_note(note_name)

        # ? Создаем виджет
        widget = NoteItem(note_name, item, self.app)
        # Сигнал удаления привязки
        widget.itemDeleted.connect(self.remove)
        self.list.setItemWidget(item, widget)
        # self.num += 1

    def remove(self, item):
        # Получить количество строк, соответствующих item
        row = self.list.indexFromItem(item).row()
        # Удалить item
        item = self.list.takeItem(row)
        # Удалить widget
        self.list.removeItemWidget(item)
        del item
