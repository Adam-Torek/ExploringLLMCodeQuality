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
    """Return True if n is prime, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """Return a list of prime factors of n."""
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def count_prime_factors(n: int) -> int:
    """Return the number of prime factors of n."""
    return len(prime_factors(n))

def count_digits(n: int) -> int:
    """Return the number of digits in n."""
    return len(str(n))

def count_digits_in_prime_factors(n: int) -> int:
    """Return the sum of the number of digits in the prime factors of n."""
    return sum(count_digits(factor) for factor in prime_factors(n))

def is_perfect_number(n: int) -> bool:
    """Return True if n is a perfect number, False otherwise."""
    sum_of_factors = sum(prime_factors(n))
    return sum_of_factors == n

def is_abundant(n: int) -> bool:
    """Return True if n is an abundant number, False otherwise."""
    return sum(prime_factors(n)) > n

def is_deficient(n: int) -> bool:
    """Return True if n is a deficient number, False otherwise."""
    return sum(prime_factors(n)) < n

def is_deficient_or_abundant(n: int) -> bool:
    """Return True if n is a deficient or abundant number, False otherwise."""
    return is_deficient(n) or is_abundant(n)

def is_amicable(a: int, b: int) -> bool:
    """Return True if a and b are amicable numbers, False otherwise."""
    return sum(prime_factors(a)) == b and sum(prime_factors(b)) == a

def is_pandigital(n: int) -> bool:
    """Return True if n is a pandigital number, False otherwise."""
    return len(set(str(n)) == set(str(range(1, len(str(n) + 1)))

def is_palindrome(n: int) -> bool:
    """Return True if n is a palindrome, False otherwise."""
    return str(n) == str(n)[::-1]

def is_prime_sum(n: int) -> bool:
    """Return True if the sum of the prime factors of n is prime, False otherwise."""
    return is_prime(sum(prime_factors(n))

def is_prime_sum_divisible_by_3(n: int) -> bool:
    """Return True if the sum of the prime factors of n is divisible by 3, False otherwise."""
    return sum(prime_factors(n)) % 3 == 0

def is_prime_sum_divisible_by_5(n: int) -> bool:
    """Return True if the sum of the prime factors of n