"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split_arr(arr, n):
    """
    Splits a list at the nth element and adds the first part to the end.

    Args:
        arr (list): The input list.
        n (int): The index of the element to split at.

    Returns:
        list: The modified list with the first part added to the end.
    """
    if len(arr) < n:
        raise IndexError("Index out of range")

    first_part = arr[:n]
    second_part = arr[n:]

    return second_part + first_part