"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""


def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False


print(check_none((10, 4, 5, 6, None)))