"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""
def new_tuple(string, list):
    """
    Create a new tuple from the given string and list
    :param string: str
    :param list: list
    :return: tuple
    """
    return tuple(string.split() + list)