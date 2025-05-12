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

# Better approach:

def fib(n: int) -> int:
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
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Test cases
print(fib(10)) # Output: 55
print(fib(1)) # Output: 1
print(fib(8)) # Output: 21

# Time complexity: O(n)
# Space complexity: O(1)

# This approach uses a loop to calculate the n-th Fibonacci number, which is more efficient than the recursive approach.