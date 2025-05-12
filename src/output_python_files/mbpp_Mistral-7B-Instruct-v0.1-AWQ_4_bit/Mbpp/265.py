"""
Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
def list_split(lst, n):
    """
    Takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
    """
    if len(lst) % n != 0:
        raise ValueError("The length of the list must be divisible by n")
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i+n])
    return result

# assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],3)==[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
# assert list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 3) == [[1, 4, 7, 10, 13, 16, 19, 22], [2, 5, 8, 11, 14, 17, 20], [3, 6, 9, 12, 15, 18, 21]]
# assert list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 4) == [[1, 5, 9, 13, 17, 21], [2, 6, 10, 14, 18, 22], [3, 7, 11, 15, 19, 23], [4, 8, 12, 16, 20, 24]]