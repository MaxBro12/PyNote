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

        'new_user_b': 'Создать аккаунт',
        'delete_user_b': '! УДАЛИТЬ АККАУНТ !',

        'set_wtkey_l': 'Путь до ключа',
        'set_wtkey_i': '',

        'set_host_l': 'Хост сервера',
        'set_host_i': '',

        'serv_st_l': 'Статус сервера',
        'serv_st_i': '',

        'set_token_l': 'Токен доступа',
        'set_token_i': '',

        'dia_new_user_exists': 'Данный пользователь уже существует',
        'dia_new_user_created': 'Пользователь {username} создан',
        'dia_delete_user_acces': 'Вы уверены что хотите удалить пользователя?',
        'dia_user_was_deleted': 'Пользователь {username} удален',
    },
    'eng': {
        'emp_title': 'Note title',
        'emp_inner':'Text...',

        'add_but': 'Add a new note',
        'settings_but': 'Settings',

        'sync_but': 'Sync note',
        'delete_but': 'Delete',

        'as_lang': 'Language',
        'as_theme': 'Theme',
        'as_opacity': 'Transparency',
        'as_text_size': 'Font size',

        'as_username': 'Login',
        'as_password': 'Password',

        'set_gen': 'Basic',
        'set_user': 'User',
        'set_server': 'Network',
        
        'set_wid_l': 'Width',
        'set_wid_i': '',

        'set_hei_l': 'Height',
        'set_hei_i': '',

        'set_opa_l': 'Transparency',
        'set_opa_i': '',

        'set_lang_l': 'Language',
        'set_lang_i': '',

        'set_theme_l': 'Theme',
        'set_theme_i': '',

        'set_title_l': 'Title Size',
        'set_title_i': '',

        'set_text_l': 'Text Size',
        'set_text_i': '',

        'set_nl_l': 'Short bookmark size',
        'set_nl_i': '',

        'set_username_l': 'User name',
        'set_username_i': '',

        'set_password_l': 'Password',
        'set_password_i': '',

        'new_user_b': 'Create an account',
        'delete_user_b': '! DELETE ACCOUNT!',

        'set_wtkey_l': 'Path to the key',
        'set_wtkey_i': '',

        'set_host_l': 'Server host',
        'set_host_i': '',

        'serv_st_l': 'Server status',
        'serv_st_i': '',

        'set_token_l': 'Access token',
        'set_token_i': '',

        'dia_new_user_exists': 'This user already exists',
        'dia_new_user_created': 'User {username} has been created',
        'dia_delete_user_acces': 'Are you sure you want to delete the user?',
        'dia_user_was_deleted': 'User {username} has been deleted',
    }
}
