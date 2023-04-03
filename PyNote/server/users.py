from requests import get, post, Response


from .urls import url


from settings import api_1, api_new, api_usr


def api_check_user(host: str, name: str) -> bool:
    return True if get(url(host, api_new, name)).json()['available'] \
        else False


def api_create_user(host: str, name: str, password: str) -> dict | Response:
    return post(
        url(host, api_new, name), data={"username": name, "password": password}
    )


def api_login_user(host: str, name: str, password: str) -> dict | Response:
    return get(
        url(host, api_usr, name), data={"username": name, "password": password}
    ).json()
