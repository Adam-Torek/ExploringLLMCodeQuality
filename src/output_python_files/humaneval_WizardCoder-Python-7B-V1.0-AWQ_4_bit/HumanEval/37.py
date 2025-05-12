def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [i for i in range(0, len(l), 2) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    return [l[i] if i % 2 == 1 else even_values.pop(0) for i in range(len(l))]


# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))


# Explanation:
# The function first creates a list of even indices using a list comprehension. Then it creates a new list of even values using another list comprehension.
# It then sorts the even values in ascending order using the sort() method. Finally, it creates a new list l' by iterating over the range of indices of l and
# checking if the index is odd or even. If the index is odd, it adds the value of l at that index to the new list. If the index is even, it adds the first value
# of the sorted even_values list to the new list. This ensures that the even values are sorted and the odd values are unchanged.
# The function returns the new list l'.