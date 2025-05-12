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
# We can define a table of size n+1 to store the values of the fibfib sequence up to that point.
# Then, we can compute the nth element of the sequence by adding up the values in the table.
# This approach has a time complexity of O(n), where n is the input value.

def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    fib_table = [0] * (n+1)
    fib_table[0] = 0
    fib_table[1] = 0
    fib_table[2] = 1

    for i in range(3, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2] + fib_table[i-3]

    return fib_table[n]

# Test cases
print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24<|endoftext|>