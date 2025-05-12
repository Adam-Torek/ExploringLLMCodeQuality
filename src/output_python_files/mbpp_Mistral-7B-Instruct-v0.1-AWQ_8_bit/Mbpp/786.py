"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""

def right_insertion(lst, val):
    """
    This function takes a sorted list and a value to insert into the list.
    It returns the index of the value in the list.
    """
    for i in range(len(lst)):
        if lst[i] == val:
            return i
        elif lst[i] < val:
            break
    return len(lst)


# Test the function
assert right_insertion([1,2,4,5],6)==4