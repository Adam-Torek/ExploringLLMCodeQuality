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
        return is_polite(n // 10) + is_polite(n % 10)


def is_polite_recursive(n):
    """
    :param n: int
    :return: int
    """
    if n < 10:
        return n
    else:
        return is_polite_recursive(n // 10) + is_polite_recursive(n % 10)


def is_polite_recursive_memo(n, memo):
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
            memo[n] = is_polite_recursive_memo(n // 10, memo) + is_polite_recursive_memo(n % 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized(n, memo):
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
            memo[n] = is_polite_recursive_memo_optimized(n // 10, memo) + is_polite_recursive_memo_optimized(n % 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_2(n, memo):
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
            memo[n] = is_polite_recursive_memo_optimized_2(n // 10, memo) + is_polite_recursive_memo_optimized_2(n % 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_3(n, memo):
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
            memo[n] = is_polite_recursive_memo_optimized_3(n // 10, memo) + is_polite_recursive_memo_optimized_3(n % 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_4(n, memo):
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
            memo[n] = is_polite_recursive_memo_optimized_4(n // 10, memo) + is_polite_recursive_memo_optimized_4(n % 10, memo)
            return memo[n]


def is_polite_recursive_memo_optimized_5(n, memo):
    """
    :param n: int
    :param memo: dict
    :return: int
    """
    if n < 10:
        return