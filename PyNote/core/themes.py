from .filemanage import create_file, get_files, pjoin
from settings import DIR_THEMES


def get_themes() -> list[str]:
    return get_files(DIR_THEMES)


def create_theme(name: str, inner: str):
    create_file(pjoin(DIR_THEMES, name), inner)

