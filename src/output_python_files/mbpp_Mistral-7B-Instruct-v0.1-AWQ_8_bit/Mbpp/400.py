"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""

def extract_freq(lst):
    """
    Extract the number of unique tuples in the given list.
    """
    # Create an empty set to store the tuples
    set_lst = set(lst)
    # Return the length of the set
    return len(set_lst)