"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False

assert check_none((10, 4, 5, 6, None)) == True
assert check_none((10, 4, 5, 6)) == False
assert check_none((None, None, None)) == True
assert check_none(()) == False
assert check_none((None,)) == True
assert check_none((None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)) == True
assert check_none((None, None,