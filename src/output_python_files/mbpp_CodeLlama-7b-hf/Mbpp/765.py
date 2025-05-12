"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""


def is_polite(n):
    """
    :param n: int
    :return: int
    """
    if n < 10:
        return n
    else:
        return is_polite(n - 1) + is_polite(n - 2)


def is_polite_recursive(n):
    """
    :param n: int
    :return: int
    """
    if n < 10:
        return n
    else:
        return is_polite_recursive(n - 1) + is_polite_recursive(n - 2)


def is_polite_memoized(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n < 10:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_memoized(n - 1, memo) + is_polite_memoized(n - 2, memo)
            return memo[n]


def is_polite_memoized_recursive(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n < 10:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_memoized_recursive(n - 1, memo) + is_polite_memoized_recursive(n - 2, memo)
            return memo[n]


def is_polite_iterative(n):
    """
    :param n: int
    :return: int
    """
    if n < 10:
        return n
    else:
        i = 1
        while i < n:
            i = is_polite_iterative(i)
        return i + is_polite_iterative(n - 1)


def is_polite_iterative_memoized(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n < 10:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            i = 1
            while i < n:
                i = is_polite_iterative_memoized(i, memo)
            memo[n] = i + is_polite_iterative_memoized(n - 1, memo)
            return memo[n]


def is_polite_iterative_memoized_recursive(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n < 10:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            i = 1
            while i < n:
                i = is_polite_iterative_memoized_recursive(i, memo)
            memo[n] = i + is_polite_iterative_memoized_recursive(n - 1, memo)
            return memo[n]


def is_polite_iterative_memoized_recursive_2(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n < 10:
        return n
    else:
        if n in memo:
            return memo[n]
        else: