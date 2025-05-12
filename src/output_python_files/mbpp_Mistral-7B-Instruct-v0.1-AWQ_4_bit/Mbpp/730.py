"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    """
    This function removes consecutive duplicates of a given list.
    """
    if len(lst) < 2:
        return lst
    else:
        i = 0
        while i < len(lst) - 1:
            if lst[i] == lst[i + 1]:
                del lst[i + 1]
            else:
                i += 1
        return lst

assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]