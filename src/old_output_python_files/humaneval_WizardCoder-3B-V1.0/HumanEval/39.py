def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

#     if n == 1:
#         return 2
#     elif n == 2:
#         return 3
#     else:
#         fib_n = 0
#         fib_n_1 = 1
#         for i in range(2, n):
#             fib_n = fib_n_1 + fib_n_1
#             fib_n_1 = fib_n - fib_n_1
#         return fib_n

#     def is_prime(num: int) -> bool:
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     fib_n = 0
#     fib_n_1 = 1
#     for i in range(2, n):
#         fib_n = fib_n_1 + fib_n_1
#         fib_n_1 = fib_n - fib_n_1
#     if is_prime(fib_n):
#         return fib_n
#     else:
#         return prime_fib(n)

#     def is_prime(num: int) -> bool:
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     fib_n = 0
#     fib_n_1 = 1
#     for i in range(2, n):
#         fib_n = fib_n_1 + fib_n_1
#         fib_n_1 = fib_n - fib_n_1
#     if is_prime(fib_n):
#         return fib_n
#     else:
#         return prime_fib(n)

#     def is_prime(num: int) -> bool:
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     fib_n = 0
#     fib_n_1 = 1
#     for i in range(2, n):
#         fib_n = fib_n_1 + fib_n_1
#         fib_n_1 = fib_n - fib_n_1
#     if is_prime(fib_n):
#         return fib_n
#     else:
#         return prime_fib(n)

#     def is_prime(num: int) -> bool:
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     fib_n = 0
#     fib_n_1 = 1
#     for i in range(2, n):
#         fib_n = fib_n_1 + fib_n_1
#         fib_n_1 = fib_n - fib_n_1
#     if is_prime(fib_n):
#         return fib_n
#     else:
#         return prime_fib(n)

#     def is_prime(num: int) -> bool:
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     fib_n = 0
#     fib_n_1 = 1
#     for i in range(2, n):
#         fib_n = fib_n_1 + fib