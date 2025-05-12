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

def modp_inv(n: int, p: int):
    """Return the inverse of n modulo p (be aware of numerics).
    >>> modp_inv(3, 5)
    2
    >>> modp_inv(1101, 101)
    1
    >>> modp_inv(0, 101)
    1
    >>> modp_inv(8, 11)
    3
    >>> modp_inv(1, 101)
    100
    """

def modp_pow(n: int, e: int, p: int):
    """Return n^e modulo p (be aware of numerics).
    >>> modp_pow(3, 3, 5)
    3
    >>> modp_pow(1101, 101, 101)
    1
    >>> modp_pow(0, 101, 101)
    1
    >>> modp_pow(8, 11, 11)
    8
    >>> modp_pow(100, 101, 101)
    1
    """

def modp_sqrt(n: int, p: int):
    """Return the square root of n modulo p (be aware of numerics).
    >>> modp_sqrt(3, 5)
    2
    >>> modp_sqrt(1101, 101)
    1
    >>> modp_sqrt(0, 101)
    1
    >>> modp_sqrt(8, 11)
    3
    >>> modp_sqrt(100, 101)
    1
    """

def modp_sqrt_inv(n: int, p: int):
    """Return the inverse of the square root of n modulo p (be aware of numerics).
    >>> modp_sqrt_inv(3, 5)
    2
    >>> modp_sqrt_inv(1101, 101)
    1
    >>> modp_sqrt_inv(0, 101)
    1
    >>> modp_sqrt_inv(8, 11)
    3
    >>> modp_sqrt_inv(100, 101)
    1
    """

def modp_sqrt_inv_all(n: int, p: int):
    """Return all square roots of n modulo p (be aware of numerics).
    >>> modp_sqrt_inv_all(3, 5)
    [2, 3]
    >>> modp_sqrt_inv_all(1101, 101)
    [1, 100]
    >>> modp_sqrt_inv_all(0, 101)
    [1, 100]
    >>> modp_sqrt_inv_all(8, 11)
    [3, 8]
    >>> modp_sqrt_inv_all(100, 101)
    [1, 100]
    """

def modp_sqrt_all(n: int, p: int):
    """Return all square roots of n modulo p (be aware of numerics).
    >>> modp_sqrt_all(3, 5)
    [2, 3]
    >>> modp_sqrt_all(1101, 101)
    [1, 100]
    >>> modp_sqrt_all(0, 101)
    [1, 100]
    >>> modp_sqrt_all(8, 11)
    [3, 8]
    >>> modp_sqrt_all(100, 101)
    [1, 100]
    """

def modp_sqrt_all_inv(n: int, p: int):
    """Return all square roots of n modulo p (be aware of numerics).
    >>> modp_sqrt_all_inv(3, 5)
    [