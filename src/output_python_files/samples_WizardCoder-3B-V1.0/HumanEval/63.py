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

# Solution:
# We can use dynamic programming to compute the nth element of the fibfib sequence.
# We can define a function fibfib(n) that takes an integer n as input and returns the nth element of the fibfib sequence.
# We can initialize two variables, fib1 and fib2, to 0 and 1, respectively.
# We can then loop through the sequence from 2 to n-1, updating the values of fib1 and fib2 as follows:
# fib1 = fib2
# fib2 = fib1 + fib2
# We can then return the value of fib2, which is the nth element of the fibfib sequence.

def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for i in range(2, n):
            fib1 = fib2
            fib2 = fib1 + fib2
        return fib2

# Test cases:
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24<|endoftext|>