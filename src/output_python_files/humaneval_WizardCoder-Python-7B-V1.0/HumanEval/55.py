def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib_iter(n: int):
    """Return n-th Fibonacci number using iterative approach.
    >>> fib_iter(10)
    55
    >>> fib_iter(1)
    1
    >>> fib_iter(8)
    21
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

def fib_matrix(n: int):
    """Return n-th Fibonacci number using matrix multiplication.
    >>> fib_matrix(10)
    55
    >>> fib_matrix(1)
    1
    >>> fib_matrix(8)
    21
    """
    if n <= 1:
        return n
    a = [[1, 1], [1, 0]]
    b = [[1, 1], [0, 1]]
    for i in range(2, n+1):
        a, b = matrix_mult(a, b)
    return a[0][0]

def matrix_mult(a, b):
    """Multiply two matrices."""
    c = [[sum(a[i][j]*b[j][k] for j in range(len(b[0])) for k in range(len(b[0]))] for i in range(len(a))]
    return [[sum(a[i][j]*b[j][k] for j in range(len(b[0])) for k in range(len(b[0]))] for i in range(len(a))]

def fib_matrix_fast(n: int):
    """Return n-th Fibonacci number using fast matrix multiplication.
    >>> fib_matrix_fast(10)
    55
    >>> fib_matrix_fast(1)
    1
    >>> fib_matrix_fast(8)
    21
    """
    if n <= 1:
        return n
    a = [[1, 1], [1, 0]]
    b = [[1, 1], [1, 0]]
    for i in range(2, n+1):
        a, b = matrix_mult_fast(a, b)
    return a[0][0]

def matrix_mult_fast(a, b):
    """Multiply two matrices."""
    c = [[sum(a[i][j]*b[j][k] for j in range(len(b[0])) for k in range(len(b[0]))] for i in range(len(a))]
    return [[sum(a[i][j]*b[j][k] for j in range(len(b[0])) for k in range(len(b[0]))] for i in range(len(a))]

def fib_matrix_fastest(n: int):
    """Return n-th Fibonacci number using fastest matrix multiplication.
    >>> fib_matrix_fastest(10)
    55
    >>> fib_matrix_fastest(1)
    1
    >>> fib_matrix_fastest(8)
    21
    """
    if n <= 1:
        return n
    a = [[1, 1], [1, 0]]
    b = [[1, 1], [1, 0]]
    for i in range(2, n