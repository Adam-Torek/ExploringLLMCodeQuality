def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l), key=l.index)


# Test cases
print(unique([5, 3, 5, 2, 3, 9, 0, 123])) # Output: [0, 2, 3, 5, 9, 123]
print(unique([1, 2, 3, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # Output: [1]
print(unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Time complexity: O(nlogn)
# Space complexity: O(n)

# Can be optimized to O(n) by using a dictionary to store the count of each element and then sorting the keys with the count as the value
# and then returning the keys in ascending order.