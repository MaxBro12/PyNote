from .notes_server import (
    sent_notes,
    upload_notes,
    serv_delete_note,
)

from .notes_local import (
    get_local_notes,
    add_local_note,
    rename_local_note,
    remove_local_note,
)


__all__ = [
    'sent_notes',
    'upload_notes',
    'serv_delete_note',

    'get_local_notes',
    'add_local_note',
    'rename_local_note',
    'remove_local_note',
]
