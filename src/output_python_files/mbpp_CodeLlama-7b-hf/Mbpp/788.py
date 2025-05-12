"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""


def new_tuple(list_: list, string: str) -> tuple:
    """
    Create a new tuple from the given string and list.
    :param list_: list
    :param string: string
    :return: tuple
    """
    return tuple(list_ + [string])


if __name__ == '__main__':
    print(new_tuple(["WEB", "is"], "best"))