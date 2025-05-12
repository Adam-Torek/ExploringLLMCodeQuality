def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if n < 0:
        n += p
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result


def test():
    """Test modp function."""
    for n in range(-10, 11):
        for p in range(1, 11):
            assert modp(n, p) == pow(2, n) % p


if __name__ == "__main__":
    test()