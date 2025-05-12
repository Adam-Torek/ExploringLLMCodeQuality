"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""

def right_insertion(lst, val):
    """
    Insert a value into a sorted list at the right position
    """
    for i in range(len(lst)):
        if lst[i] == val:
            return i
        elif lst[i] < val:
            break
    return len(lst)


# Test
lst = [1, 2, 4, 5]
assert right_insertion(lst, 6) == 4