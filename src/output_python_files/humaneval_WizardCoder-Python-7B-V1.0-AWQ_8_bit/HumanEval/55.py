def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Test cases
print(fib(10)) # Output: 55
print(fib(1)) # Output: 1
print(fib(8)) # Output: 21


# Time complexity: O(2^n)
# Space complexity: O(n)


# Better solution using memoization

def fib_memo(n: int, memo: dict = {}) -> int:
    """Return n-th Fibonacci number using memoization.
    >>> fib_memo(10)
    55
    >>> fib_memo(1)
    1
    >>> fib_memo(8)
    21
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

# Test cases
print(fib_memo(10)) # Output: 55
print(fib_memo(1)) # Output: 1
print(fib_memo(8)) # Output: 21

# Time complexity: O(n)
# Space complexity: O(n)

# Better solution using matrix exponentiation

def matrix_mult(a, b, mod):
    result = [[0, 0], [0, 0]]
    a11, a12, a21, a22 = a
    b11, b12, b21, b22 = b
    result[0][0] = (a11 * b11 + a12 * b21) % mod
    result[0][1] = (a11 * b12 + a12 * b22) % mod
    result[1][0] = (a21 * b11 + a22 * b21) % mod
    result[1][1] = (a21 * b12 + a22 * b22) % mod
    return result

def matrix_pow(matrix, n, mod):
    if n == 1:
        return matrix
    if n % 2 == 0:
        square = matrix_pow(matrix, n // 2, mod)
        return matrix_mult(square, square, mod)
    else:
        return matrix_mult(matrix_mult(matrix, matrix, mod), matrix_pow(matrix, n // 2, mod), mod)

def fib_matrix(n: int, mod: int = 10**9 + 7) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = [[1, 1], [1, 0]]
        return matrix_pow(matrix, n - 1, mod)[0][0]

# Test cases
print(fib_matrix(10)) # Output: 55
print(fib_matrix(1)) # Output: 1
print(fib_matrix(8)) # Output: 21

# Time complexity: O(log n)
# Space complexity: O(1)

# Better solution using Binet's formula

from math import sqrt, pi, cos, sin, floor

def fibonacci(n: int) -> int:
    sqrt5 = sqrt(5)
    psi = (1 + sqrt5) / 2
    phi = (1 + sqrt5) / 2
    return floor((phi**n - (-phi)**(-n)) / sqrt5)

# Test cases
print(fibonacci(10)) # Output: 55
print(fibonacci(1)) # Output: