"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""

def get_equal(lst):
    if len(set(len(t) for t in lst)) == 1:
        return True
    else:
        return False

# Test cases
print(get_equal([(11, 22, 33), (44, 55, 66)])) # True
print(get_equal([(1, 2, 3), (4, 5, 6, 7), (8, 9)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)])) # False
print(get_equal([(1, 2), (3, 4, 5), (6, 7, 8, 9)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])) # True
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19, 20)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19, 20), (21, 22, 23, 24, 25)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19, 20), (21, 22, 23, 24, 25, 26)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19, 20), (21, 22, 23, 24, 25, 26, 27)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12, 13, 14), (15, 16, 17, 18, 19, 20), (21, 22, 23, 24, 25, 26, 27, 28)])) # False
print(get_equal([(1, 2, 3), (4, 5, 6), (7, 8,