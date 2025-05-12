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
        return "Error: n must be greater than 0"
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

# Test cases
print(special_factorial(4))
print(special_factorial(5))
print(special_factorial(0))
print(special_factorial(10))