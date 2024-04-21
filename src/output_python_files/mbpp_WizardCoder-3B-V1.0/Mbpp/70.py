"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""

def get_equal(tuples):
    if len(set(len(t) for t in tuples)) == 1:
        return True
    else:
        return False

# Test cases
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(11, 22), (44, 55, 66)]) == False
assert get_equal([(11, 22, 33), (44, 55)]) == False<|endoftext|>