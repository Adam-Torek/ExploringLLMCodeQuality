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
# We first create a list of even indices using a list comprehension. Then, we create a list of even values using another list comprehension.
# We sort the even values using the sort() method. Finally, we iterate over the indices of the original list and return the original value if the index is odd,
# otherwise we return the next value from the sorted even values list. We use the pop() method to remove the values from the even values list as we iterate.
# This ensures that we don't modify the original list.