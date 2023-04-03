import requests


from settings import api_1, api_new, api_usr


def check_user(name: str):
    print(requests.get(api_1 + api_new + name).json())


def create_user(name: str, password: str):
    print(api_1 + api_new + name)
    ans = requests.post(
        api_1 + api_new + name, {'username': name, 'password': password}
    )
    print(ans.json())
