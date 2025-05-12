"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""


def count_Primes_nums(num):
    """
    :param num: non-negative number
    :return: number of prime numbers less than the given non-negative number
    """
    if num < 2:
        return 0
    count = 0
    for i in range(2, num + 1):
        if is_prime(i):
            count += 1
    return count


def is_prime(num):
    """
    :param num: non-negative number
    :return: True if num is prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(count_Primes_nums(5))
    print(count_Primes_nums(10))
    print(count_Primes_nums(15))
    print(count_Primes_nums(20))
    print(count_Primes_nums(25))
    print(count_Primes_nums(30))
    print(count_Primes_nums(35))
    print(count_Primes_nums(40))
    print(count_Primes_nums(45))
    print(count_Primes_nums(50))
    print(count_Primes_nums(55))
    print(count_Primes_nums(60))
    print(count_Primes_nums(65))
    print(count_Primes_nums(70))
    print(count_Primes_nums(75))
    print(count_Primes_nums(80))
    print(count_Primes_nums(85))
    print(count_Primes_nums(90))
    print(count_Primes_nums(95))
    print(count_Primes_nums(100))
    print(count_Primes_nums(105))
    print(count_Primes_nums(110))
    print(count_Primes_nums(115))
    print(count_Primes_nums(120))
    print(count_Primes_nums(125))
    print(count_Primes_nums(130))
    print(count_Primes_nums(135))
    print(count_Primes_nums(140))
    print(count_Primes_nums(145))
    print(count_Primes_nums(150))
    print(count_Primes_nums(155))
    print(count_Primes_nums(160))
    print(count_Primes_nums(165))
    print(count_Primes_nums(170))
    print(count_Primes_nums(175))
    print(count_Primes_nums(180))
    print(count_Primes_nums(185))
    print(count_Primes_nums(190))
    print(count_Primes_nums(195))
    print(count_Primes_nums(200))
    print(count_Primes_nums(205))
    print(count_Primes_nums(210))
    print(count_Primes_nums(215))
    print(count_Primes_nums(220))
    print(count_Primes_nums(225))
    print(count_Primes_nums(230))
    print(count_Primes_nums(235))
    print(count_Primes_nums(240))
    print(count_Primes_nums(245))
    print(count_Primes_nums(250))
    print