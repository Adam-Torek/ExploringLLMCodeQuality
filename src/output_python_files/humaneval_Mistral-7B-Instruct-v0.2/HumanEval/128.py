def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if len(arr) == 0:
        return None

    sign = 1
    prod = 1
    for num in arr:
        prod *= sign
        sign *= (1 if num > 0 else -1)

    return prod * sum(abs(num) for num in arr)

# Testing
if __name__ == '__main__':
    import doctest
    doctest.testmod()