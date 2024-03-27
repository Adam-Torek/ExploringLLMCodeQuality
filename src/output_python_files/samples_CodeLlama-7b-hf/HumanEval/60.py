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
    """sum_to_n_recursive is a function that sums numbers from 1 to n.
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


def sum_to_n_recursive_memo(n: int):
    """sum_to_n_recursive_memo is a function that sums numbers from 1 to n.
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
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = i + memo[i - 1]
    return memo[n]


def sum_to_n_recursive_memo_2(n: int):
    """sum_to_n_recursive_memo_2 is a function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo_2(30)
    465
    >>> sum_to_n_recursive_memo_2(100)
    5050
    >>> sum_to_n_recursive_memo_2(5)
    15
    >>> sum_to_n_recursive_memo_2(10)
    55
    >>> sum_to_n_recursive_memo_2(1)
    1
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = i + memo[i - 1]
    return memo[n]


def sum_to_n_recursive_memo_3(n: int):
    """sum_to_n_recursive_memo_3 is a function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo_3(30)
    465
    >>> sum_to_n_recursive_memo_3(100)
    5050
    >>> sum_to_n_recursive_memo_3(5)
    15
    >>> sum_to_n_recursive_memo_3(10)
    55
    >>> sum_to_n_recursive_memo_3(1)
    1
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = i + memo[i - 1]
    return memo[n]


def sum_to_n_recursive_