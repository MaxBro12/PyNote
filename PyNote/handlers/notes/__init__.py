from .notes_server import (
    sent_notes,
    upload_notes,
    serv_delete_note,
)

from .notes_local import (
    get_local_notes,
)


__all__ = [
    'sent_notes',
    'upload_notes',
    'serv_delete_note',

    'get_local_notes',
]
