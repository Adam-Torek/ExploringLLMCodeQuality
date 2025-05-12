"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(tup):
    result = []
    for i in tup:
        if type(i) == tuple:
            result.append(extract_even(i))
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4), 6, 8))