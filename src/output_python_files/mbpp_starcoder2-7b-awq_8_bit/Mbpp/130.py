"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""

def max_occurrences(l):
    """
    >>> max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])
    2
    """
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return max(d, key=d.get)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/python_fundamentals/python_fundamentals_pt2/python_fundamentals_pt2.py
"""
Python Fundamentals II
"""

# 1.
def print_list_of_lists(list_of_lists):
    """
    >>> print_list_of_lists([[1,2], [3,4], [5,6,7]])
    1 2
    3 4
    5 6 7
    """
    for i in list_of_lists:
        for j in i:
            print(j, end=" ")
        print()

# 2.
def flatten(list_of_lists):
    """
    >>> flatten([[1,2], [3,4], [5,6,7]])
    [1, 2, 3, 4, 5, 6, 7]
    """
    return [i for j in list_of_lists for i in j]

# 3.
def merge(list1, list2):
    """
    >>> merge([1,2,3], [4,5,6])
    [1, 2, 3, 4, 5, 6]
    """
    return list1 + list2

# 4.
def merge_sort(list_of_lists):
    """
    >>> merge_sort([[5,2,3], [4,1], [6,7,3]])
    [[2, 3, 4, 5], [1, 6, 7, 3]]
    """
    return [sorted(i) for i in list_of_lists]

# 5.
def remove_dups(list_of_lists):
    """
    >>> remove_dups([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]])
    [[1, 2], [3, 4], [5, 6], [7]]
    """
    return [list(set(i)) for i in list_of_lists]

# 6.
def mode(list_of_lists):
    """
    >>> mode([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]])
    [3, 4, 5, 6]
    """
    return [i for i in list_of_lists if list_of_lists.count(i) == max(list_of_lists.count(i))]

# 7.
def sum_of_lists(list_of_lists):
    """
    >>> sum_of_lists([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]])
    42
    """
    return sum([sum(i) for i in list_of_lists])

# 8.
def remove_odd_indices(list_of_lists):
    """
    >>> remove_odd_indices([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]])
    [[2], [4], [6]]
    """
    return [i[1::2] for i in list_of_lists]

# 9.
def remove_every_other(list_of_lists):
    """
    >>> remove_every_other([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]])
    [[1, 3, 5], [2, 4, 6]]
    """
    return [i[::2] for i in list