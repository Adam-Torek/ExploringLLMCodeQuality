"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""


def is_polite(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    else:
        return n * 9 + 10


def is_polite_recursive(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    else:
        return n * 9 + 10


def is_polite_recursive_memo(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = n * 9 + 10
            return memo[n]


def is_polite_recursive_memo_optimized(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_recursive_memo_optimized(n * 9 + 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_2(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_recursive_memo_optimized_2(n * 9 + 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_3(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_recursive_memo_optimized_3(n * 9 + 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_4(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_recursive_memo_optimized_4(n * 9 + 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_5(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = is_polite_recursive_memo_optimized_5(n * 9 + 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_6(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n == 1:
        return 1
    else:
        if n in memo:
            return memo[n]
        else: