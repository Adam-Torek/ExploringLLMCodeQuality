"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""

def get_equal(tuples):
    if len(tuples) == 0:
        return True
    else:
        length = len(tuples[0])
        for tup in tuples:
            if len(tup) != length:
                return False
        return True

# Test cases
print(get_equal([(11, 22, 33), (44, 55, 66)])) # True
print(get_equal([(11, 22, 33), (44, 55, 66, 77)])) # False
print(get_equal([(11, 22), (44, 55, 66)])) # False
print(get_equal([])) # True
print(get_equal([()])) # True
print(get_equal([(11, 22, 33), (44, 55), (66, 77, 88, 99)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100)])) # False
print(get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99, 100, 111)]) # False