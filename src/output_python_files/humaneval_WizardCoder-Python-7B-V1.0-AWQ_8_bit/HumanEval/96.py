def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Test cases
print(count_up_to(5)) # [2,3]
print(count_up_to(11)) # [2,3,5,7]
print(count_up_to(0)) # []
print(count_up_to(20)) # [2,3,5,7,11,13,17,19]
print(count_up_to(1)) # []
print(count_up_to(18)) # [2,3,5,7,11,13,17]