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

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is a prime number, False otherwise.
    for example:
    is_prime(5) => True
    is_prime(11) => True
    is_prime(0) => False
    is_prime(20) => True
    is_prime(1) => False
    is_prime(18) => True
    """

def count_primes(n):
    """Implement a function that takes an non-negative integer n and returns the number of prime numbers less than n.
    for example:
    count_primes(5) => 2
    count_primes(11) => 4
    count_primes(0) => 0
    count_primes(20) => 8
    count_primes(1) => 0
    count_primes(18) => 4
    """

def count_divisors(n):
    """Implement a function that takes an integer n and returns the number of divisors of n.
    A divisor of an integer n is an integer that divides n evenly.
    for example:
    count_divisors(5) => 1
    count_divisors(11) => 2
    count_divisors(0) => 0
    count_divisors(20) => 2
    count_divisors(1) => 1
    count_divisors(18) => 2
    """

def count_divisors_up_to(n):
    """Implement a function that takes an integer n and returns the number of divisors of n up to n.
    A divisor of an integer n is an integer that divides n evenly.
    for example:
    count_divisors_up_to(5) => 1
    count_divisors_up_to(11) => 2
    count_divisors_up_to(0) => 0
    count_divisors_up_to(20) => 2
    count_divisors_up_to(1) => 1
    count_divisors_up_to(18) => 2
    """

def count_divisors_below(n):
    """Implement a function that takes an integer n and returns the number of divisors of n below n.
    A divisor of an integer n is an integer that divides n evenly.
    for example:
    count_divisors_below(5) => 1
    count_divisors_below(11) => 2
    count_divisors_below(0) => 0
    count_divisors_below(20) => 2
    count_divisors_below(1) => 1
    count_divisors_below(18) => 2
    """

def count_divisors_between(a, b):
    """Implement a function that takes two integers a and b and returns the number of divisors of a and b.
    A divisor of an integer n is an integer that divides n evenly.
    for example:
    count_divisors_between(5, 10) => 3
    count_divisors_between(11, 15) => 4
    count_divisors_between(0, 20) => 2
    count_divisors_between(1, 18) => 2
    """

def count_divisors_in_range(a, b):
    """Implement a function that takes two integers a and b and returns the number of divisors of all integers between a and b.
    A divisor of an integer n is an integer that divides n evenly.
    for example:
    count_divisors_in_range(5, 10)