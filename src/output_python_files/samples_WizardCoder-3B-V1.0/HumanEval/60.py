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

#     # Using a loop to sum numbers from 1 to n
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total

#     # Using recursion to sum numbers from 1 to n
#     def sum_helper(n):
#         if n == 0:
#             return 0
#         else:
#             return n + sum_helper(n-1)
#     return sum_helper(n)

    # Using a generator expression to sum numbers from 1 to n
    return sum(range(1, n+1))

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1<|endoftext|>