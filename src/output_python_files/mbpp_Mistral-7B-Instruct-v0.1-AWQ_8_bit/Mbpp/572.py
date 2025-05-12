"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

def two_unique_nums(lst):
    """
    This function takes a list of numbers as an input and returns a new list with
    only two unique numbers.
    """
    # create a set from the list to remove duplicates
    set_lst = set(lst)
    # convert the set back to a list and return
    return list(set_lst)

# test the function
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]