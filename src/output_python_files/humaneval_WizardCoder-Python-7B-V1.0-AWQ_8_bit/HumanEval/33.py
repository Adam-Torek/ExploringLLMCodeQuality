def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_new = []
    for i in range(len(l)):
        if i % 3 != 0:
            l_new.append(l[i])
    l_new.sort()
    return l_new


# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))


# Explanation:
# The function first creates a new list l_new and appends all the elements of l that are not divisible by three to it.
# Then it sorts the list l_new. Finally, it returns the sorted list l_new.