def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)


#%%

def fibfib_memo(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence using memoization.
    >>> fibfib_memo(1)
    0
    >>> fibfib_memo(5)
    4
    >>> fibfib_memo(8)
    24
    """
    memo = [0, 0, 1]
    if n <= 0:
        return 0
    elif n == 1:
        return memo[0]
    elif n == 2:
        return memo[1]
    else:
        memo.append(memo[n-1] + memo[n-2] + memo[n-3])
        return memo[n-1]


#%%

def fibfib_memo_iter(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence using memoization and iteration.
    >>> fibfib_memo_iter(1)
    0
    >>> fibfib_memo_iter(5)
    4
    >>> fibfib_memo_iter(8)
    24
    """
    memo = [0, 0, 1]
    if n <= 0:
        return 0
    elif n == 1:
        return memo[0]
    elif n == 2:
        return memo[1]
    else:
        memo.append(memo[n-1] + memo[n-2] + memo[n-3])
        for i in range(n-2, -1, -1):
            memo[i] = memo[i+1] + memo[i+2] + memo[i+3]
        return memo[0]


#%%

def fibfib_memo_recursive(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence using memoization and recursion.
    >>> fib