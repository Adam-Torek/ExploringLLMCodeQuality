"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(tuple1, tuple2):
    if len(tuple1)!= len(tuple2):
        return False
    for i in range(len(tuple1)):
        if tuple1[i] >= tuple2[i]:
            return False
    return True

assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((1, 2, 3), (1, 2, 3)) == True
assert check_smaller((1, 2, 3), (1, 2, 4)) == True
assert check_smaller((1, 2, 3), (1, 2, 2)) == True
assert check_smaller((1, 2, 3), (1, 2, 1)) == True
assert check_smaller((1, 2, 3), (1, 1, 1)) == True
assert check_smaller((1, 2, 3), (1, 0, 1)) == True
assert check_smaller((1, 2, 3), (0, 0, 0)) == True
assert check_smaller((1, 2, 3), (0, 0, 1)) == True
assert check_smaller((1, 2, 3), (0, 1, 1)) == True
assert check_smaller((1, 2, 3), (0, 1, 2)) == True
assert check_smaller((1, 2, 3), (0, 2, 2)) == True
assert check_smaller((1, 2, 3), (0, 2, 3)) == True
assert check_smaller((1, 2, 3), (0, 3, 3)) == True
assert check_smaller((1, 2, 3), (0, 3, 4)) == True
assert check_smaller((1, 2, 3), (0, 4, 4)) == True
assert check_smaller((1, 2, 3), (0, 4, 5)) == True
assert check_smaller((1, 2, 3), (0, 5, 5)) == True
assert check_smaller((1, 2, 3), (0, 5, 6)) == True
assert check_smaller((1, 2, 3), (0, 6, 6)) == True
assert check_smaller((1, 2, 3), (0, 6, 7)) == True
assert check_smaller((1, 2, 3), (0, 7, 7)) == True
assert check_smaller((1, 2, 3), (0, 7, 8)) == True
assert check_smaller((1, 2, 3), (0, 8, 8)) == True
assert check_smaller((1, 2, 3), (0, 8, 9)) == True
assert check_smaller((1, 2, 3), (0, 9, 9)) == True
assert check_smaller((1, 2, 3), (0, 9, 10)) == True
assert check_smaller((1, 2, 3), (0, 10, 10)) == True
assert check_smaller((1, 2, 3), (0, 10, 11)) == True
assert check_smaller((1, 2, 3), (0, 11, 11)) == True
assert check_smaller((1, 2, 3), (0, 11, 12)) == True
assert check_smaller((1, 2, 3), (0, 12, 12)) == True
assert check_smaller((1, 2, 3), (0, 12, 13)) == True
assert check_smaller((1, 2, 3), (0, 13, 13)) == True
assert check_smaller((1, 2, 3), (0, 13, 14)) == True
assert check_smaller((1, 2, 3), (0, 14,