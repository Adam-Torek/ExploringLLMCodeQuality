"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""

def pancake_sort(lst):
    """
    This function takes a list of elements and sorts them in ascending order.
    """
    # First, we find the maximum element in the list
    max_elem = max(lst)

    # Then, we iterate over the list and swap each element with the maximum element
    for i in range(len(lst)):
        lst[i], max_elem = max_elem, lst[i]

    return lst


# Test the function
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]