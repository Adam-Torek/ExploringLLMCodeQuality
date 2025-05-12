def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(1, n + 1))


def sum_to_n_recursive(n: int):
    """sum_to_n_recursive is a recursive function that sums numbers from 1 to n.
    >>> sum_to_n_recursive(30)
    465
    >>> sum_to_n_recursive(100)
    5050
    >>> sum_to_n_recursive(5)
    15
    >>> sum_to_n_recursive(10)
    55
    >>> sum_to_n_recursive(1)
    1
    """
    if n == 1:
        return 1
    else:
        return n + sum_to_n_recursive(n - 1)


def sum_to_n_recursive_memo(n: int, memo: dict = None):
    """sum_to_n_recursive_memo is a recursive function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo(30)
    465
    >>> sum_to_n_recursive_memo(100)
    5050
    >>> sum_to_n_recursive_memo(5)
    15
    >>> sum_to_n_recursive_memo(10)
    55
    >>> sum_to_n_recursive_memo(1)
    1
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    else:
        memo[n] = n + sum_to_n_recursive_memo(n - 1, memo)
        return memo[n]


def sum_to_n_recursive_memo_optimized(n: int, memo: dict = None):
    """sum_to_n_recursive_memo_optimized is a recursive function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo_optimized(30)
    465
    >>> sum_to_n_recursive_memo_optimized(100)
    5050
    >>> sum_to_n_recursive_memo_optimized(5)
    15
    >>> sum_to_n_recursive_memo_optimized(10)
    55
    >>> sum_to_n_recursive_memo_optimized(1)
    1
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    else:
        memo[n] = n + sum_to_n_recursive_memo_optimized(n - 1, memo)
        return memo[n]


def sum_to_n_recursive_memo_optimized_2(n: int, memo: dict = None):
    """sum_to_n_recursive_memo_optimized_2 is a recursive function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo_optimized_2(30)
    465
    >>> sum_to_n_recursive_memo_optimized_2(100)
    5050
    >>> sum_to_n_