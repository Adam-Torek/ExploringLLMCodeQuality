"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
def extract_even(nested_tuple):
    result = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            result.append(extract_even(element))
        elif isinstance(element, int):
            if element % 2 == 0:
                result.append(element)
    return tuple(result)

assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)