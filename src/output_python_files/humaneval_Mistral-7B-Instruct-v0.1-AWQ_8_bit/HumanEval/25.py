from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    if n % 3 == 0:
        return [3] + factorize(n // 3)
    else:
        return []


def factorize_with_repeats(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize_with_repeats(8)
    [2, 2, 2]
    >>> factorize_with_repeats(25)
    [5, 5]
    >>> factorize_with_repeats(70)
    [2, 5, 7]
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize_with_repeats(n // 2)
    if n % 3 == 0:
        return [3] + factorize_with_repeats(n // 3)
    else:
        return []


def factorize_with_repeats_and_order(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize_with_repeats_and_order(8)
    [2, 2, 2]
    >>> factorize_with_repeats_and_order(25)
    [5, 5]
    >>> factorize_with_repeats_and_order(70)
    [2, 5, 7]
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize_with_repeats_and_order(n // 2)
    if n % 3 == 0:
        return [3] + factorize_with_repeats_and_order(n // 3)
    else:
        return []


def factorize_with_repeats_and_order_and_return_dict(n: int) -> dict:
    """ Return dictionary of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize_with_repeats_and_order_and_return_dict(8)
    {2: 3}
    >>> factorize_with_repeats_and_order_and_return_dict(25)
    {5: 2}
    >>> factorize_with_repeats_and_order_and_return_dict(70)
    {2: 1, 5: 1, 7: 1}
    """
    if n == 1:
        return {}
    if n == 2:
        return {2: 1}
    if n % 2 == 0:
        return {2: 1} + factorize_with_repeats_and_order_and_return_dict(n // 2