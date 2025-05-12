def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i


def is_prime(n: int) -> bool:
    """ Check if a number is prime or not
    >>> is_prime(7)
    True
    >>> is_prime(12)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """ Find the prime factors of a number
    >>> prime_factors(15)
    [3, 5]
    """
    factors = []
    divisor = 2
    while n > 1:
        if is_prime(divisor) and n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor = largest_divisor(n)
    return factors

def main():
    n = int(input("Enter a number: "))
    print(prime_factors(n))

if __name__ == "__main__":
    main()