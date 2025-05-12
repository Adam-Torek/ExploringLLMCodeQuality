"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    """
    >>> bell_number(2)
    2
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number(n-1) + sum([bell_number(k)*bell_number(n-1-k) for k in range(n)])

def bell_number_memo(n):
    """
    >>> bell_number_memo(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1, 1:1}
    def helper(n):
        if n not in cache:
            cache[n] = bell_number_memo(n-1) + sum([bell_number_memo(k)*bell_number_memo(n-1-k) for k in range(n)])
        return cache[n]
    return helper(n)

def bell_number_iter(n):
    """
    >>> bell_number_iter(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1, 1:1}
    def helper(n):
        if n not in cache:
            cache[n] = bell_number_iter(n-1) + sum([bell_number_iter(k)*bell_number_iter(n-1-k) for k in range(n)])
        return cache[n]
    return helper(n)

def bell_number_iter_memo(n):
    """
    >>> bell_number_iter_memo(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1, 1:1}
    def helper(n):
        if n not in cache:
            cache[n] = bell_number_iter_memo(n-1) + sum([bell_number_iter_memo(k)*bell_number_iter_memo(n-1-k) for k in range(n)])
        return cache[n]
    return helper(n)

def bell_number_iter_memo_fast(n):
    """
    >>> bell_number_iter_memo_fast(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1, 1:1}
    def helper(n):
        if n not in cache:
            cache[n] = bell_number_iter_memo_fast(n-1) + sum([bell_number_iter_memo_fast(k)*bell_number_iter_memo_fast(n-1-k) for k in range(n)])
        return cache[n]
    return helper(n)

def bell_number_iter_memo_fast_fast(n):
    """
    >>> bell_number_iter_memo_fast_fast(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1, 1:1}
    def helper(n):
        if n not in cache:
            cache[n] = bell_number_iter_memo_fast_fast(n-1) + sum([bell_number_iter_memo_fast_fast(k)*bell_number_iter_memo_fast_fast(n-1-k) for k in range(n)])
        return cache[n]
    return helper(n)

def bell_number_iter_memo_fast_fast_fast(n):
    """
    >>> bell_number_iter_memo_fast_fast_fast(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1, 1:1}
    def helper(n):
        if n not in cache:
            cache[n] = bell_number_iter_memo_fast_fast_fast(n-1) + sum([bell_number_iter_memo_fast_fast_fast(k)*bell_number_iter_memo_fast_fast_fast(n-1-k) for k in range(n)])
        return cache[n]
    return helper(n)

def bell_number_iter_memo_fast_fast_fast_fast(n):
    """
    >>> bell_number_iter_memo_fast_fast_fast_fast(2)
    2
    """
    "*** YOUR CODE HERE ***"
    cache = {0:1,