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
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n-1)


def sum_to_n_iterative(n: int):
    """sum_to_n_iterative is a function that sums numbers from 1 to n using a loop.
    >>> sum_to_n_iterative(30)
    465
    >>> sum_to_n_iterative(100)
    5050
    >>> sum_to_n_iterative(5)
    15
    >>> sum_to_n_iterative(10)
    55
    >>> sum_to_n_iterative(1)
    1
    """
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def sum_to_n_recursive(n: int):
    """sum_to_n_recursive is a function that sums numbers from 1 to n using recursion.
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
        return n + sum_to_n_recursive(n-1)


def sum_to_n_recursive_memo(n: int):
    """sum_to_n_recursive_memo is a function that sums numbers from 1 to n using recursion and memoization.
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
    memo = {}
    if n in memo:
        return memo[n]
    else:
        result = n + sum_to_n_recursive_memo(n-1)
        memo[n] = result
        return result


def sum_to_n_recursive_memo_tail(n: int):
    """sum_to_n_recursive_memo_tail is a function that sums numbers from 1 to n using recursion and memoization with tail recursion.
    >>> sum_to_n_recursive_memo_tail(30)
    465
    >>> sum_to_n_recursive_memo_tail(100)
    5050
    >>> sum_to_n_recursive_memo_tail(5)
    15
    >>> sum_to_n_recursive_memo_tail(10)
    55
    >>> sum_to_n_recursive_memo_tail(1)
    1
    """
    memo = {}
    if n in memo:
        return memo[n]
    else:
        result = sum_to_n_recursive_mem