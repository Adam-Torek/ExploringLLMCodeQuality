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
    if n < 0:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return []
    else:
        prime_list = []
        for i in range(2, n):
            if is_prime(i):
                prime_list.append(i)
        return prime_list


def is_prime(n):
    """Implement a function that takes an integer and returns True if it is prime, False otherwise.
    for example:
    is_prime(2) => True
    is_prime(3) => True
    is_prime(4) => False
    is_prime(5) => True
    is_prime(6) => False
    is_prime(7) => True
    is_prime(8) => False
    is_prime(9) => False
    is_prime(10) => False
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def count_down_from(n):
    """Implement a function that takes an integer and returns an array of the first n integers that are
    prime numbers and greater than n.
    for example:
    count_down_from(5) => [7,5]
    count_down_from(11) => [13,11]
    count_down_from(0) => []
    count_down_from(20) => [19,17,13,11,7]
    count_down_from(1) => []
    count_down_from(18) => [17,13,7]
    """
    if n < 0:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return []
    else:
        prime_list = []
        for i in range(n, 0, -1):
            if is_prime(i):
                prime_list.append(i)
        return prime_list


def count_down_from_to(n, m):
    """Implement a function that takes two integers and returns an array of the first n integers that are
    prime numbers and greater than m.
    for example:
    count_down_from_to(5, 10) => [7,9,5]
    count_down_from_to(11, 11) => []
    count_down_from_to(0, 20) => [19,17,13,11,7]
    count_down_from_to(1, 18) => [17,13,7]
    count_down_from_to(18, 18) => []
    """
    if n < 0:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return []
    elif m < 0:
        return []
    elif m == 0:
        return []
    elif m == 1:
        return []
    else:
        prime_list = []
        for i in range(m, n, -1):
            if is_prime(i):
                prime_list.append(