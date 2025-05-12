"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""

def tup_string(tuple_):
    """
    Convert a tuple to a string.
    """
    string_ = tuple_
    for i in range(len(tuple_)):
        string_ = string_[:i] + "," + string_[i:]
    return string_

assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")