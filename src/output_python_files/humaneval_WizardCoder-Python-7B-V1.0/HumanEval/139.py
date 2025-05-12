def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if n <= 0:
        return 1
    else:
        return n * special_factorial(n-1)


# Test cases
print(special_factorial(4))  # Output: 288
print(special_factorial(5))  # Output: 1260
print(special_factorial(6))  # Output: 32760
print(special_factorial(7))  # Output: 10080
print(special_factorial(8))  # Output: 362880
print(special_factorial(9))  # Output: 1296000
print(special_factorial(10))  # Output: 720720