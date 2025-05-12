"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap_List(lst):
    """
    This function takes a list as an input and returns a new list with the first and last elements interchanged.
    """
    # Using slicing to get the first and last elements of the list
    first_element = lst[0]
    last_element = lst[-1]

    # Using slicing to remove the first and last elements from the list
    lst = lst[1:-1]

    # Using the extend method to add the first and last elements to the list
    lst.extend([last_element, first_element])

    # Returning the new list
    return lst

# Testing the function
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]