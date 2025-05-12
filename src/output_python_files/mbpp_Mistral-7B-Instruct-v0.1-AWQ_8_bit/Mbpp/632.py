"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(lst):
    """
    This function takes a list as an input and returns a new list with all zeroes moved to the end.
    """
    new_lst = []
    for i in lst:
        if i != 0:
            new_lst.append(i)
    new_lst.extend(lst[lst.index(0):])
    return new_lst

# Test the function
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]