"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""
def rear_extract(lst):
    """
    Function that takes in a list of tuples and returns a list containing the rear element of each tuple.
    """
    return [i[1] for i in lst]

# Test the function
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]</s>