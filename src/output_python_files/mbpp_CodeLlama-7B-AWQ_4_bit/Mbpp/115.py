"""
Write a function to check whether all dictionaries in a list are empty or not.
assert empty_dit([{},{},{}])==True
"""


def empty_dit(list_of_dicts):
    for i in list_of_dicts:
        if i:
            return False
    return True


print(empty_dit([{},{},{}