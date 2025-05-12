"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""

def split_Arr(lst, n):
    """
    This function takes a list and an integer n as input and returns a new list
    that is the first n elements of the original list followed by the rest of the list.
    """
    if n > len(lst):
        return lst
    else:
        return lst[:n] + lst[n:]


# Test the function
print(split_Arr([12,10,5,6,52,36],2))