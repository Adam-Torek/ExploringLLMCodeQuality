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
    """ Check if a given number is prime or not.
    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """ Return a list of prime factors of a given number.
    >>> prime_factors(12)
    [2, 2, 3]
    """
    factors = []
    divisor = 2
    while n > 1:
        if is_prime(divisor) and n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def gcd(a: int, b: int) -> int:
    """ Return the greatest common divisor of two numbers.
    >>> gcd(12, 8)
    4
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    """ Return the least common multiple of two numbers.
    >>> lcm(12, 8)
    24
    """
    return a * b // gcd(a, b)

def is_square(n: int) -> bool:
    """ Check if a given number is a square number or not.
    >>> is_square(9)
    True
    >>> is_square(10)
    False
    """
    return int(n**0.5)**2 == n

def is_perfect_square(n: int) -> bool:
    """ Check if a given number is a perfect square or not.
    >>> is_perfect_square(9)
    True
    >>> is_perfect_square(10)
    False
    """
    return int(n**0.5)**2 == n

def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    """ Check if a, b, c are Pythagorean triplet.
    >>> is_pythagorean_triplet(3, 4, 5)
    True
    >>> is_pythagorean_triplet(5, 12, 13)
    False
    """
    return a**2 + b**2 == c**2

def is_pythagorean_triplet_with_sum(a: int, b: int, c: int, target: int) -> bool:
    """ Check if a, b, c are Pythagorean triplet with a+b+c=target.
    >>> is_pythagorean_triplet_with_sum(3, 4, 5, 10)
    True
    >>> is_pythagorean_triplet_with_sum(5, 12, 13, 16)
    False
    """
    return a+b+c == target and is_pythagorean_triplet(a, b, c)

def is_pythagorean_triplet_with_product(a: int, b: int, c: int, target: int) -> bool:
    """ Check if a, b, c are Pythagorean triplet with a*b*c=target.
    >>>