"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""

def split_Arr(lst, n):
    """
    This function takes a list and an integer n as input and returns a new list
    where the first n elements are concatenated to the end of the list.
    """
    return lst[:n] + lst[n:]


# Test the function
print(split_Arr([12,10,5,6,52,36],2))