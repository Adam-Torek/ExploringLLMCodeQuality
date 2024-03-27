def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

#     for i in range(1, n):
#         if n % i == 0:
#             return i
#     return n

#     # Alternative approach using trial division
#     for i in range(2, n):
#         if n % i == 0:
#             return i
#     return n

#     # Alternative approach using trial division with early exit
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return i
#     return n

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n] = n
#         return n

#     return helper(n)

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n] = n
#         return n

#     return helper(n)

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n] = n
#         return n

#     return helper(n)

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n] = n
#         return n

#     return helper(n)

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n] = n
#         return n

#     return helper(n)

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n] = n
#         return n

#     return helper(n)

#     # Alternative approach using trial division with early exit and memoization
#     memo = {}
#     def helper(n: int) -> int:
#         if n in memo:
#             return memo[n]
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 memo[n] = i
#                 return i
#         memo[n]