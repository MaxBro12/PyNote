class Stack:
    """Реализация Stack"""
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    @property
    def stack(self):
        return self.__stack

    @property
    def size(self):
        return len(self.__stack)

    def __len__(self):
        return len(self.__stack)
