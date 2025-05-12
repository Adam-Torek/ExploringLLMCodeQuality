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
    return pow(2, n, p)


def modp_list(n: int, p: int, length: int):
    """Return a list of 2^n modulo p for each index in range(length).
    >>> modp_list(3, 5, 5)
    [3, 2, 4, 1, 3, 2]
    >>> modp_list(1101, 101, 5)
    [2, 1, 4, 100, 1, 2]
    >>> modp_list(0, 101, 5)
    [1, 1, 1, 1, 1, 1]
    """
    return [modp(n, p) for _ in range(length)]

def modp_matrix(n: int, p: int, rows: int, cols: int):
    """Return a matrix of 2^n modulo p for each element in range(rows*cols).
    >>> modp_matrix(3, 5, 2, 3)
    [[3, 2, 4], [1, 3, 2]]
    >>> modp_matrix(1101, 101, 2, 3)
    [[2, 1, 4], [1, 100, 2]]
    >>> modp_matrix(0, 101, 2, 3)
    [[1, 1, 1], [1, 1, 1]]
    """
    return [modp_list(n, p, cols) for _ in range(rows)]

def modp_matrix_list(n: int, p: int, rows: int, cols: int):
    """Return a list of matrices of 2^n modulo p for each index in range(rows*cols).
    >>> modp_matrix_list(3, 5, 2, 3)
    [[[3, 2, 4], [1, 3, 2], [3, 2, 4]], [[1, 3, 2], [1, 3, 2], [1, 3, 2]]]
    >>> modp_matrix_list(1101, 101, 2, 3)
    [[[2, 1, 4], [1, 100, 2], [2, 4, 1]], [[1, 1, 4], [1, 1, 2], [2, 4, 1]]]
    >>> modp_matrix_list(0, 101, 2, 3)
    [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
    """
    return [modp_matrix(n, p, rows, cols) for _ in range(rows*cols)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()