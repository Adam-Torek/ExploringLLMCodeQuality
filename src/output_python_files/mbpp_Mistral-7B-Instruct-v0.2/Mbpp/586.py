"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split_arr(arr, n):
    """
    Splits a list at the nth element and adds the first part to the end.

    :param arr: List to be split
    :param n: Index of the element to split at
    :return: List with the first part at the end
    """
    if len(arr) < n:
        raise IndexError("Index out of range")
    first_part = arr[:n]
    second_part = arr[n:]
    return second_part + first_part

# Test the function
assert split_arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
assert split_arr([1,2,3,4],3) == [4,1,2,3]
assert split_arr([], 0) == []
assert split_arr([], 1) == []
assert split_arr([], 2) == []
assert split_arr([1], 0) == [1]
assert split_arr([1], 1) == [1]
assert split_arr([1], 2) == [1]
assert split_arr([1,2], 0) == [2,1]
assert split_arr([1,2], 1) == [2]
assert split_arr([1,2], 2) == [1]</s>