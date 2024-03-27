"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""
def tup_string(tuple):
    """
    Converts a tuple to a string
    :param tuple: tuple to be converted
    :return: string representation of the tuple
    """
    return ''.join(tuple)

assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"</s>