from typing import TypedDict


class Phrases(TypedDict):
    emp_title: str
    emp_inner: str

    add_but: str
    settings_but: str

    sync_but: str
    delete_but: str


class Lang(TypedDict):
    ru: Phrases
    eng: Phrases


lang: Lang = {
    'ru': {
        'emp_title': 'Название заметки',
        'emp_inner': 'Текст...',

        'add_but': 'Добавить новую заметку',
        'settings_but': 'Настройки',

        'sync_but': 'Синхронизировать заметку',
        'delete_but': 'Удалить',
    },
    'eng': {
        'emp_title': 'Название заметки',
        'emp_inner': 'Текст...',

        'add_but': 'Добавить новую заметку',
        'settings_but': 'Настройки',

        'sync_but': 'Синхронизировать заметку',
        'delete_but': 'Удалить',
    }
}
