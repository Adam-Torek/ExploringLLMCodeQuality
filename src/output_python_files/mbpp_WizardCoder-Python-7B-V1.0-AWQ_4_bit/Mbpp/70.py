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
print(get_equal([(11, 22, 33), (44, 55, 66, 77)])) # False
print(get_equal([(11, 22, 33), (44, 55)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 15, 16, 17, 18)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 15, 16, 17)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 15, 16, 17), (18, 19, 20)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 15, 16, 17), (18, 19, 20), (21, 22, 23)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 15, 16, 17), (18, 19, 20), (21, 22, 23, 24)])) # True
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 15, 16, 17), (18, 19, 20), (21, 22, 23, 24), (25, 26, 27)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 12, 13), (14, 1