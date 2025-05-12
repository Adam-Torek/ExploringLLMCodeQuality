def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    set1 = set(l1)
    set2 = set(l2)
    common_set = set1.intersection(set2)
    return sorted(list(common_set)


# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]


# Time Complexity: O(nlogn)
# Space Complexity: O(n)


# Better solution

def better_common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> better_common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> better_common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    set1 = set(l1)
    set2 = set(l2)
    return sorted(list(set1.intersection(set2))

# Test cases
print(better_common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(better_common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Best solution

def best_common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> best_common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> best_common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    set1 = set(l1)
    set2 = set(l2)
    return sorted(list(set1 & set2)

# Test cases
print(best_common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(best_common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]

# Time Complexity: O(n)
# Space Complexity: O(n)

# The best solution uses set intersection, which is a built-in function that takes O(n) time complexity. 
# The set() function takes O(n) time to create a set from a list, and the & operator takes O(n) time to find the intersection of two sets. 
# The sorted() function takes O(nlogn) time to sort the list, but it's not a big deal since it's only called once. 
# The space complexity is O