def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

#     if len(l) < 2:
#         return True

#     for i in range(len(l) - 1):
#         if l[i] > l[i + 1]:
#             return False
#         elif l[i] < l[i + 1]:
#             return True

#     return True

    if len(l) < 2:
        return True

    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
        elif l[i] < l[i + 1]:
            return True

    return True

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True<|endoftext|>