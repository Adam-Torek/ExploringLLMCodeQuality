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
    factors = []
    i = 3
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append(i)
            factors.append(count)
        i += 1
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors


def factorize_iterative(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize_iterative(8)
    [2, 2, 2]
    >>> factorize_iterative(25)
    [5, 5]
    >>> factorize_iterative(70)
    [2, 5, 7]
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append(i)
            factors.append(count)
        i += 1
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors


def factorize_recursive(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize_recursive(8)
    [2, 2, 2]
    >>> factorize_recursive(25)
    [5, 5]
    >>> factorize_recursive(70)
    [2, 5, 7]
    """
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize_recursive(n // 2)
    factors = []
    i = 3
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append(i)
            factors.append(count)
        i += 1
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors


def test_factorize():
    for n in [8, 25, 70, 10000000000000000000]:
        assert factorize(n) == factorize_iterative(n) == factorize_recursive(n)


if __name__ == "__main__":
    test_factorize()