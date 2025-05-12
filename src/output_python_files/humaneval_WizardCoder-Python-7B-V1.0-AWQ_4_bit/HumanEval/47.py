def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2] + l[n//2-1]) / 2
    else:
        return l[n//2]


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 100, 10, 20]))  # Output: 15.0


# Test cases:
print(median([1, 2, 3, 4, 5]))  # Output: 3
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: 5
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: 5.5
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # Output: 6
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # Output: 6.5
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))  # Output: 7
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))  # Output: 7.5
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # Output: 8
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))  # Output: 8.5
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))  # Output: 9
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))  # Output: 9.5
print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))  # Output: 10
print(median([1, 2, 3, 4, 5, 6, 7,