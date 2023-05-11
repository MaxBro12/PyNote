from server import (
    api_save_note,
    api_delete_note,
    api_get_notes,
)


from spec_types import (
    User_Data,
    User_Note,
    Delete_Note,

    Note,

    Config_server
)


def serv_save_note(server: Config_server, data: User_Note) -> bool:
    return api_save_note(server['host'], server['token'], data)


def serv_delete_note(server: Config_server, data: Delete_Note) -> bool:
    return api_delete_note(server['host'], server['token'], data)


def serv_get_notes(
        server: Config_server, data: User_Data | None
) -> list[Note]:
    if data is None:
        return []
    ans = api_get_notes(server['host'], server['token'], data)
    if ans is not None:
        return ans
    else:
        return []
