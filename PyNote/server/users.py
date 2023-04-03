from requests import get, post


from .urls import url


from settings import api_1, api_new, api_usr


def check_user(name: str) -> bool:
    return True if get(url(api_1, api_new, name)).json()['available'] \
        else False


def create_user(name: str, password: str):
    return post(
        url(api_1, api_new, name), data={"username": name, "password": password}
    )
