def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def is_prime(n: int) -> bool:
    """
    Check if a given number is prime or not.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_square(n: int) -> bool:
    """
    Check if a given number is a square number or not.
    """
    return int(n**0.5)**2 == n

def is_cube(n: int) -> bool:
    """
    Check if a given number is a cube or not.
    """
    return int(n**(1/3))**3 == n

def is_perfect_square(n: int) -> bool:
    """
    Check if a given number is a perfect square or not.
    """
    return int(n**0.5)**2 == n

def is_perfect_cube(n: int) -> bool:
    """
    Check if a given number is a perfect cube or not.
    """
    return int(n**(1/3))**3 == n

def is_pandigital(n: int) -> bool:
    """
    Check if a given number is a pandigital number or not.
    """
    return len(str(n)) == 9 and sorted(str(n)) == sorted(list(range(1,10)))

def is_palindrome(n: int) -> bool:
    """
    Check if a given number is a palindrome or not.
    """
    return str(n) == str(n)[::-1]

def is_pandigital_prime(n: int) -> bool:
    """
    Check if a given number is a pandigital prime or not.
    """
    return is_pandigital(n) and is_prime(n)

def is_pandigital_prime_palindrome(n: int) -> bool:
    """
    Check if a given number is a pandigital prime palindrome or not.
    """
    return is_pandigital(n) and is_prime(n) and is_palindrome(n)

def is_prime_power(n: int) -> bool:
    """
    Check if a given number is a prime power or not.
    """
    return is_prime(n) and is_cube(n)

def is_prime_power_palindrome(n: int) -> bool:
    """
    Check if a given number is a prime power palindrome or not.
    """
    return is_prime_power(n) and is_palindrome(n)

def is_prime_cube(n: int) -> bool:
    """
    Check if a given number is a prime cube or not.
    """
    return is_prime(n) and is_cube(n)

def is_prime_square(n: int) -> bool:
    """
    Check if a given number is a prime square or not.
    """
    return is_prime(n) and is_square(n)

def is_prime_square_palindrome(n: int) -> bool:
    """
    Check if a given number is a prime square palindrome or not.
    """
    return is_prime_square(n) and is_palindrome(n)

def is_prime_cube_palindrome(n: int) -> bool:
    """
    Check if a given number is a prime cube palindrome or not.
    """
    return is_prime_cube(n) and is_palindrome(n)

def is_pandigital_prime_power(n: int) -> bool: