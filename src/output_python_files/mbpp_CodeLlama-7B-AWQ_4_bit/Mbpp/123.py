"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""


def amicable_numbers_sum(n):
    """
    :param n: int
    :return: int
    """
    sum_of_amicable_numbers = 0
    for i in range(1, n + 1):
        if i == sum_of_divisors(i):
            if sum_of_divisors(i) == i:
                continue
            if sum_of_divisors(i) == sum_of_divisors(sum_of_divisors(i)):
                sum_of_amicable_numbers += i
    return sum_of_amicable_numbers


def sum_of_divisors(n):
    """
    :param n: int
    :return: int
    """
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors


if __name__ == '__main__':
    print(amicable_numbers_sum(999))
    print(amicable_numbers_sum(10000))
    print(amicable_numbers_sum(100000))
    print(amicable_numbers_sum(1000000))
    print(amicable_numbers_sum(10000000))
    print(amicable_numbers_sum(100000000))
    print(amicable_numbers_sum(1000000000))
    print(amicable_numbers_sum(10000000000))
    print(amicable_numbers_sum(100000000000))
    print(amicable_numbers_sum(1000000000000))
    print(amicable_numbers_sum(10000000000000))
    print(amicable_numbers_sum(100000000000000))
    print(amicable_numbers_sum(1000000000000000))
    print(amicable_numbers_sum(10000000000000000))
    print(amicable_numbers_sum(100000000000000000))
    print(amicable_numbers_sum(1000000000000000000))
    print(amicable_numbers_sum(10000000000000000000))
    print(amicable_numbers_sum(100000000000000000000))
    print(amicable_numbers_sum(1000000000000000000000))
    print(amicable_numbers_sum(10000000000000000000000))
    print(amicable_numbers_sum(100000000000000000000000))
    print(amicable_numbers_sum(1000000000000000000000000))
    print(amicable_numbers_sum(10000000000000000000000000))
    print(amicable_numbers_sum(100000000000000000000000000))
    print(amicable_numbers_sum(10000000000