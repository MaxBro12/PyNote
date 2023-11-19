from core import (
    create_log,
    wayfinder,
    get_files,
    pjoin,

    write_to_toml,
    read_toml,
    update_dict_to_type,
    toml_type_check,

    create_folder,
)

from settings import (
    DIR_DATA,
    DIR_THEMES,
    DIR_NOTES,

    FILE_SETTINGS,
    FILE_SETTINGS_IN,

    FILE_TH_DARK,
    FILE_TH_DARK_IN,
    FILE_TH_LIGHT,
    FILE_TH_LIGHT_IN,
    FILE_TH_SPACE,
    FILE_TH_SPACE_IN,
)


def main_check():
    # ? Проверяем папку с данными
    check_data()
    # ? Проверяем файл конфига
    check_conf()
    # ? Проверяем папку с заметками
    check_notes()
    # ? Проверяем папку с темами
    check_themes_dir()


def create_settings() -> bool:
    write_to_toml(FILE_SETTINGS_IN, FILE_SETTINGS)
    create_log(f'FILE {FILE_SETTINGS} CREATED!', 'info')
    return True


def check_data():
    if not wayfinder(DIR_DATA):
        create_folder(DIR_DATA)


def check_notes():
    if not wayfinder(DIR_NOTES):
        create_folder(DIR_NOTES)


def check_themes_dir():
    if not wayfinder(DIR_THEMES):
        create_folder(DIR_THEMES)


def check_conf():
    if not wayfinder(FILE_SETTINGS):
        create_settings()
    else:
        if not toml_type_check(FILE_SETTINGS_IN, read_toml(FILE_SETTINGS)):
            create_settings()
            create_log(f'FILE {FILE_SETTINGS} OVERWRITTEN!', 'error')

