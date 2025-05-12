"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""

def tuple_to_dict(tup):
    return dict(zip(tup[::2], tup[1::2]))

# Test the function
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}