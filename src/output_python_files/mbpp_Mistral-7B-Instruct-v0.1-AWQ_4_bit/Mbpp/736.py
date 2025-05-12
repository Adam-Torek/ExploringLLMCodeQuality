"""
Write a function to locate the left insertion point for a specified value in sorted order. https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-24.php
assert left_insertion([1,2,4,5],6)==4
"""

def left_insertion(lst, val):
    """
    This function takes a list and a value and returns the index of the left insertion point for the value in the list.
    """
    for i in range(len(lst)):
        if lst[i] > val:
            return i
    return len(lst)