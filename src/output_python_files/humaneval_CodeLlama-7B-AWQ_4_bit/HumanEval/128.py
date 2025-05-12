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
    if not arr:
        return None
    else:
        return sum(abs(x) for x in arr) * prod(sign(x) for x in arr)


def sign(x):
    """
    Returns 1 if x > 0, -1 if x < 0, 0 if x == 0.
    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def prod(arr):
    """
    Returns product of all elements in array.
    """
    if not arr:
        return 1
    else:
        return reduce(lambda x, y: x * y, arr)


def test_prod_signs():
    assert prod_signs([1, 2, 2, -4]) == -9
    assert prod_signs([0, 1]) == 0
    assert prod_signs([]) is None


if __name__ == '__main__':
    test_prod_signs()