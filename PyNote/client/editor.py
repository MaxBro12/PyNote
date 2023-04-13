from PySide6.QtWidgets import (
    QVBoxLayout,

    QLineEdit,
    QTextEdit,

    QListWidgetItem,
    QWidget,
)


from handlers import (
    rename_local_note,
    save_local_note,
)


class Editor(QVBoxLayout):
    def __init__(self):
        # ! Основа
        super().__init__()
        # self.widget_i = None

        # ? Редактор названия
        self.title_e = QLineEdit()
        # self.title_e.setText(widget.name)
        self.title_e.editingFinished.connect(self.slot_rename_note)
        self.title_e.setFixedHeight(30)
        self.title_e.setTextMargins(5, 0, 0, 0)
        self.title_e.setMaxLength(20)

        # ? Редактор текста
        self.text_e = QTextEdit()
        self.text_e.textChanged.connect(self.slot_save_note)
        # self.text_e.setText(widget.inner)
        # self.text_e.setTextMargins(5, 0, 0, 0)

        # ? Добавляем все в лайаут
        self.addWidget(self.title_e, 1)
        self.addWidget(self.text_e, 0)

    def update_info(self, widget):
        self.widget_i = widget
        self.title_e.setText(self.widget_i.name)
        self.text_e.setText(self.widget_i.inner)

    def slot_save_note(self):
        save_local_note(
            self.title_e.text(),
            self.text_e.toPlainText()
        )

    def slot_rename_note(self):
        self.widget_i.slot_text_changed(self.title_e.text())
