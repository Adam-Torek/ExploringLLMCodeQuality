"""
Write a function to sort a list of elements.
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
"""

def pancake_sort(lst):
    """
    This function sorts a list of elements in ascending order.
    """
    # Find the maximum element in the list
    max_elem = max(lst)

    # Find the index of the maximum element in the list
    max_index = lst.index(max_elem)

    # Sort the list by swapping the maximum element with the first element
    lst = lst[:max_index] + lst[max_index+1:]

    # Sort the list again using the built-in sort function
    lst.sort()

    # Return the sorted list
    return lst

# Test the function
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]