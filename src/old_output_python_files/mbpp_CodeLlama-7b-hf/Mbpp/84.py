"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""


def sequence(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(sequence(n - 1)) + sequence(n - sequence(n - 1))


def sequence_recursive(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_recursive(sequence_recursive(n - 1)) + sequence_recursive(n - sequence_recursive(n - 1))


def sequence_memo(n):
    """
    :param n: int
    :return: int
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n + 1):
        memo[i] = memo[sequence_memo(i - 1)] + memo[i - sequence_memo(i - 1)]
    return memo[n]


def sequence_iterative(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


def sequence_iterative_memo(n):
    """
    :param n: int
    :return: int
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def sequence_iterative_memo_2(n):
    """
    :param n: int
    :return: int
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def sequence_iterative_memo_3(n):
    """
    :param n: int
    :return: int
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def sequence_iterative_memo_4(n):
    """
    :param n: int
    :return: int
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
        memo[i] = b
    return memo[n]


def sequence_iterative_memo_5(n):
    """
    :param n: int
    :return: int
    """
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    a = 1
    b = 1
    for i in range(3, n + 1