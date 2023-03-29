from random import randint


from settings import (
    token_len,
)


def create_id() -> int:
    return randint(100_000, 999_999)


def create_token() -> str:
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    num = '0123456789'
    sumb = '!@#$%^&*()_-+='
    all_s = letters + num

    ans = ''

    for _ in range(token_len):
        ans += all_s[randint(0, len(all_s)) - 1]
    return ans
