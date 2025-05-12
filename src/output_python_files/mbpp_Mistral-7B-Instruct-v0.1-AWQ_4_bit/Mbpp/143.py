"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""

def find_lists(tuple):
    count = 0
    for i in tuple:
        if isinstance(i, list):
            count += 1
    return count

# assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2