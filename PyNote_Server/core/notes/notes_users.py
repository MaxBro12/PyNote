from core.filemanage import (
    create_folder,
    remove_dir_tree,

    pjoin,
)


from settings import DIR_NOTES


def create_userdir(username: str) -> bool:
    return create_folder(pjoin(DIR_NOTES, username))


def delete_userdir(username: str) -> bool:
    return remove_dir_tree(
        pjoin(DIR_NOTES, username)
    )
