def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

#     return all(x < t for x in l)
#     # or
#     return all(x <= t for x in l)
#     # or
#     return all(x < t for x in l) and all(x >= t for x in l)
#     # or
#     return all(x < t for x in l) or all(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) or any(x >= t for x in l)
#     # or
#     return any(x < t for x in l) and any(x >= t for x in l)
#     # or
#