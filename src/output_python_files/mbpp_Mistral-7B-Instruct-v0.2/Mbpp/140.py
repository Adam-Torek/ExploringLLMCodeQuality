"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""
def extract_singly(nested_list):
    """
    Extracts all the elements from nested list and returns a set of those elements
    """
    return set(sum(sublist, [])) for sublist in nested_list

assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])