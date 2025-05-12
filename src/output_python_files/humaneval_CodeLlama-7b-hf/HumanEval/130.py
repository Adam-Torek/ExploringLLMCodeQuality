def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        return [1, 3, 2] + tri(n - 1)


def tri_rec(n):
    """
    >>> tri_rec(3)
    [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        return [1, 3, 2] + tri_rec(n - 1)


def tri_rec_2(n):
    """
    >>> tri_rec_2(3)
    [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        return [1, 3, 2] + tri_rec_2(n - 1)


def tri_rec_3(n):
    """
    >>> tri_rec_3(3)
    [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        return [1, 3, 2] + tri_rec_3(n - 1)


def tri_rec_4(n):
    """
    >>> tri_rec_4(3)
    [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    elif n == 2:
        return [1, 3, 2]
    else:
        return [1, 3, 2] + tri_rec_4(n - 1)


def tri_rec_5(n):
    """
    >>> tri_rec_5(3)
    [1, 3,