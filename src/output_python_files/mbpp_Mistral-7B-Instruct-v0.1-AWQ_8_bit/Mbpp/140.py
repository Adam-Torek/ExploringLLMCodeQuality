"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""

def extract_singly(lst):
    """
    Flatten a list of lists into a single set of numbers.
    """
    flat_lst = []
    for sublist in lst:
        flat_lst += sublist
    return flat_lst