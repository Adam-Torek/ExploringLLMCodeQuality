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
print(check_none((10, 4, 5, 6, 7)))
print(check_none((10, 4, 5, 6, 7, None)))
print(check_none((10, 4, 5, 6, 7, 8, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, None)))
print(check_none((10, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21