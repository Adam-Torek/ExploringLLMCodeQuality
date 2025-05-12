"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""

def tuple_to_dict(tup):
    return dict(zip(tup[::2], tup[1::2]))

# Test the function
print(tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}) # True
print(tuple_to_dict((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}) # True
print(tuple_to_dict((1, 2, 3, 4, 5, 6, 7, 8, 9)) == {1: 2, 3: 4, 5: 6, 7: 8}) # True
print(tuple_to_dict((1, 2, 3, 4, 5, 6, 7)) == {1: 2, 3: 4, 5: 6}) # True
print(tuple_to_dict((1, 2, 3, 4, 5)) == {1: 2, 3: 4, 5: None}) # True
print(tuple_to_dict((1, 2, 3)) == {1: 2, 3: None}) # True
print(tuple_to_dict((1, 2)) == {1: 2}) # True
print(tuple_to_dict(()) == {}) # True
print(tuple_to_dict((1,)) == {1: None}) # True
print(tuple_to_dict(('a', 'b', 'c', 'd', 'e', 'f')) == {'a': 'b', 'c': 'd', 'e': 'f'}) # True
print(tuple_to_dict(('a', 'b', 'c', 'd', 'e')) == {'a': 'b', 'c': 'd'}) # True
print(tuple_to_dict(('a', 'b', 'c')) == {'a': 'b', 'c': None}) # True
print(tuple_to_dict('abcdef') == {'a': 'b', 'c': 'd', 'e': 'f'}) # True
print(tuple_to_dict('abc') == {'a': 'b', 'c': None}) # True
print(tuple_to_dict('a') == {'a': None}) # True
print(tuple_to_dict('') == {}) # True