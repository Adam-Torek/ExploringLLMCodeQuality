"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""
def remove_elements(list_to_remove, elements_to_remove):
    """
    :param list_to_remove: list
    :param elements_to_remove: list
    :return: list
    """
    return list(set(list_to_remove) - set(elements_to_remove))

assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
assert remove_elements([], []) == []
assert remove_elements([], [1]) == []
assert remove_elements([1], []) == [1]
assert remove_elements([1, 1], [1]) == [1]
assert remove_elements([1, 1], [2]) == [1]
assert remove_elements([1, 1, 2, 2], [1, 2]) == [2]
assert remove_elements([1, 1, 2, 2], [2, 2]) == [1]
assert remove_elements([1, 1, 2, 2], [3]) == [1, 1, 2]
assert remove_elements([1, 1, 2, 2], [3, 3]) == [1, 1, 2]
assert remove_elements([1, 1, 2, 2], []) == [1, 1, 2, 2]
assert remove_elements([], [1, 1, 2, 2]) == []
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2]) == []
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2]) == [2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2]) == [2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2]) == [2, 2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2, 2, 2]
assert remove_elements([1, 1, 2, 2], [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 2