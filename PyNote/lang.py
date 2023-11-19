from typing import TypedDict


class Phrases(TypedDict):
    emp_title: str
    emp_inner: str

    add_but: str
    settings_but: str

    sync_but: str
    delete_but: str

    # = Настройки
    as_lang: str
    as_theme: str
    as_opacity: str
    as_text_size: str

    as_username: str
    as_password: str


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

        'as_lang': 'Язык',
        'as_theme': 'Тема',
        'as_opacity': 'Прозрачность',
        'as_text_size': 'Размер шрифта',

        'as_username': 'Логин',
        'as_password': 'Пароль',
    },
    'eng': {
        'emp_title': 'Название заметки',
        'emp_inner': 'Текст...',

        'add_but': 'Добавить новую заметку',
        'settings_but': 'Настройки',

        'sync_but': 'Синхронизировать заметку',
        'delete_but': 'Удалить',

        'as_lang': '',
        'as_theme': '',
        'as_opacity': '',
        'as_text_size': '',

        'as_username': '',
        'as_password': '',
    }
}
