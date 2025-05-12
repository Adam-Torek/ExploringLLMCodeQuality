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
    return n + sum_to_n_recursive(n - 1)


def sum_to_n_recursive_memo(n: int):
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
    memo = [0] * (n + 1)

    def _sum_to_n_recursive_memo(n: int):
        if memo[n] == 0:
            if n == 1:
                memo[n] = 1
            else:
                memo[n] = n + _sum_to_n_recursive_memo(n - 1)
        return memo[n]

    return _sum_to_n_recursive_memo(n)


def sum_to_n_recursive_memo_dict(n: int):
    """sum_to_n_recursive_memo_dict is a recursive function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo_dict(30)
    465
    >>> sum_to_n_recursive_memo_dict(100)
    5050
    >>> sum_to_n_recursive_memo_dict(5)
    15
    >>> sum_to_n_recursive_memo_dict(10)
    55
    >>> sum_to_n_recursive_memo_dict(1)
    1
    """
    memo = {}

    def _sum_to_n_recursive_memo_dict(n: int):
        if n not in memo:
            if n == 1:
                memo[n] = 1
            else:
                memo[n] = n + _sum_to_n_recursive_memo_dict(n - 1)
        return memo[n]

    return _sum_to_n_recursive_memo_dict(n)


def sum_to_n_recursive_memo_list(n: int):
    """sum_to_n_recursive_memo_list is a recursive function that sums numbers from 1 to n.
    >>> sum_to_n_recursive_memo_list(30)
    465
    >>> sum_to_n_