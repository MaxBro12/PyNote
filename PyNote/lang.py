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


lang = {
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

        'set_gen': 'Основное',
        'set_user': 'Пользователь',
        'set_server': 'Сеть',
        
        'set_wid_l': 'Ширина',
        'set_wid_i': '',

        'set_hei_l': 'Высота',
        'set_hei_i': '',

        'set_opa_l': 'Прозрачность',
        'set_opa_i': '',

        'set_lang_l': 'Язык',
        'set_lang_i': '',

        'set_theme_l': 'Тема',
        'set_theme_i': '',

        'set_title_l': 'Размер Заголовка',
        'set_title_i': '',

        'set_text_l': 'Размер Текста',
        'set_text_i': '',

        'set_nl_l': 'Размер коротких закладок',
        'set_nl_i': '',

        'set_username_l': 'Имя пользователя',
        'set_username_i': '',
        'set_password_l': 'Пароль',
        'set_password_i': '',
        'set_wtkey_l': 'Путь до ключа',
        'set_wtkey_i': '',

        'set_host_l': 'Хост сервера',
        'set_host_i': '',

        'set_token_l': 'Токен доступа',
        'set_token_i': '',
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
