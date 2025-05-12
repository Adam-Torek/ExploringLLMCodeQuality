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
    prime_list = []
    for i in range(2,n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime and False otherwise.
    for example:
    is_prime(2) => True
    is_prime(11) => True
    is_prime(12) => False
    is_prime(1) => False
    is_prime(0) => False
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime and False otherwise.
    for example:
    is_prime(2) => True
    is_prime(11) => True
    is_prime(12) => False
    is_prime(1) => False
    is_prime(0) => False
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime and False otherwise.
    for example:
    is_prime(2) => True
    is_prime(11) => True
    is_prime(12) => False
    is_prime(1) => False
    is_prime(0) => False
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime and False otherwise.
    for example:
    is_prime(2) => True
    is_prime(11) => True
    is_prime(12) => False
    is_prime(1) => False
    is_prime(0) => False
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime and False otherwise.
    for example:
    is_prime(2) => True
    is_prime(11) => True
    is_prime(12) => False
    is_prime(1) => False
    is_prime(0) => False
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime and False otherwise.
    for example:
    is_prime(2) => True
    is_prime(11) => True
    is_prime(12) => False
    is_prime(1) =>