from .notes import (
    sent_notes,
    upload_notes,
    serv_delete_note,

    get_local_notes,
    add_local_note,
    save_local_note,
    rename_local_note,
    remove_local_note,
)
from .servers import (
    login_user,
    create_user,

    serv_get_notes,
    serv_save_note,
    serv_delete_note,
)


__all__ = [
    'sent_notes',
    'upload_notes',
    'serv_delete_note',

    'get_local_notes',
    'add_local_note',
    'save_local_note',
    'rename_local_note',
    'remove_local_note',
]
