"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""

def extract_freq(lst):
    """
    This function takes a list of tuples as input and returns the number of unique tuples in the list.
    """
    # create an empty set to store the tuples
    set_lst = set(lst)
    # return the length of the set
    return len(set_lst)