"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(input_list, k):
    """
    Function to remove the k'th element from a given list
    :param input_list: List to be modified
    :param k: Index of the element to be removed
    :return: List with the k'th element removed
    """
    if len(input_list) < k:
        raise IndexError("Index out of range")
    return input_list[:k] + input_list[k+1:]

# Testing the function
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
assert remove_kth_element([1,1,2,3,4,4,5,1],0)==[1, 1, 2, 3, 4, 4, 5]
assert remove_kth_element([1,1,2,3,4,4,5,1],7)==[1, 1, 2, 3, 4, 4, 5]
assert remove_kth_element([],3)==[]
assert remove_kth_element([1],3)==[]
assert remove_kth_element([1],0)==[]
assert remove_kth_element([],0)==[]