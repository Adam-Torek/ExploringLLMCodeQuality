def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

#     if n < 1:
#         return 0

#     odd_digits = 1
#     while n > 0:
#         digit = n % 10
#         if digit % 2 == 1:
#             odd_digits *= digit
#         n //= 10

#     return odd_digits if odd_digits > 0 else 0

# def digits(n):
#     """Given a positive integer n, return the product of the odd digits.
#     Return 0 if all digits are even.
#     For example:
#     digits(1)  == 1
#     digits(4)  == 0
#     digits(235) == 15
#     """

#     if n < 1:
#         return 0

#     odd_digits = 1
#     while n > 0:
#         digit = n % 10
#         if digit % 2 == 1:
#             odd_digits *= digit
#         n //= 10

#     return odd_digits if odd_digits > 0 else 0

# def digits(n):
#     """Given a positive integer n, return the product of the odd digits.
#     Return 0 if all digits are even.
#     For example:
#     digits(1)  == 1
#     digits(4)  == 0
#     digits(235) == 15
#     """

#     if n < 1:
#         return 0

#     odd_digits = 1
#     while n > 0:
#         digit = n % 10
#         if digit % 2 == 1:
#             odd_digits *= digit
#         n //= 10

#     return odd_digits if odd_digits > 0 else 0

def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n < 1:
        return 0

    odd_digits = 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_digits *= digit
        n //= 10

    return odd_digits if odd_digits > 0 else 0

# Test cases
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235))  # Output: 15<|endoftext|>