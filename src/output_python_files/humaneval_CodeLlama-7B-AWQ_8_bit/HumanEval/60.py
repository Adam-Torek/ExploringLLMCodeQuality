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


def sum_to_n_memo(n: int):
    """sum_to_n_memo is a memoized function that sums numbers from 1 to n.
    >>> sum_to_n_memo(30)
    465
    >>> sum_to_n_memo(100)
    5050
    >>> sum_to_n_memo(5)
    15
    >>> sum_to_n_memo(10)
    55
    >>> sum_to_n_memo(1)
    1
    """
    memo = {}

    def sum_to_n_memo_helper(n: int):
        if n not in memo:
            if n == 1:
                memo[n] = 1
            else:
                memo[n] = n + sum_to_n_memo_helper(n - 1)
        return memo[n]

    return sum_to_n_memo_helper(n)


def sum_to_n_memo_decorator(func):
    """sum_to_n_memo_decorator is a decorator that memoizes a function.
    >>> @sum_to_n_memo_decorator
    ... def sum_to_n_memo_decorator_helper(n: int):
    ...     if n == 1:
    ...         return 1
    ...     else:
    ...         return n + sum_to_n_memo_decorator_helper(n - 1)
    >>> sum_to_n_memo_decorator_helper(30)
    465
    >>> sum_to_n_memo_decorator_helper(100)
    5050
    >>> sum_to_n_memo_decorator_helper(5)
    15
    >>> sum_to_n_memo_decorator_helper(10)
    55
    >>> sum_to_n_memo_decorator_helper(1)
    1
    """
    memo = {}

    def sum_to_n_memo_decorator_helper(n: int):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]

    return sum_to_n_memo_decorator_helper


@sum_to_n_memo_decorator
def sum_to_n_memo_decorator_helper(n: int):
    if n == 1:
        return 1
    else:
        return n + sum_to_n_memo_decorator_helper(n - 1)


def sum_to_n_memo_decorator_helper_2(n: int):
    """sum_to_n_memo_decorator_helper_2 is a memoized function that sums numbers from 1 to n.
    >>> sum_to