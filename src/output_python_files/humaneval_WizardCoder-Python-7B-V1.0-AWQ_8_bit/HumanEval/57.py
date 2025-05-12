def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))


# Test cases
print(monotonic([1, 2, 4, 20])) # True
print(monotonic([1, 20, 4, 10])) # False
print(monotonic([4, 1, 0, -10])) # True
print(monotonic([1, 2, 1, 2, 3])) # True
print(monotonic([1, 2, 3, 2, 1])) # False
print(monotonic([1, 2, 3, 4, 5])) # True
print(monotonic([5, 4, 3, 2, 1])) # False
print(monotonic([1, 1, 1, 1])) # True
print(monotonic([1, 1, 2, 1])) # False
print(monotonic([1, 2, 1, 2, 1])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0])) # True
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3])) # True
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5])) # True
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 6])) # False
print(monotonic([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5])) # True