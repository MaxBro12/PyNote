from socket import socket, AF_INET, SOCK_DGRAM


def get_local_ip():
    """Получаем локальный IP"""
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ans = sock.getsockname()
    sock.close()
    return ans[0]
