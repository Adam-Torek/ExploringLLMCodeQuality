def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        a, b, c = 0, 1, 1
        for _ in range(n - 3):
            c = a + b
            a, b = b, c
        return c


if __name__ == "__main__":
    import doctest
    doctest.testmod()</s>