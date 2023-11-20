from .filemanage import create_file, get_files
from settings import DIR_THEMES

def get_themes() -> list[str]:
    return get_files(DIR_THEMES)

