"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""


def amicable_numbers_sum(n):
    """
    :param n: int
    :return: int
    """
    sum_ = 0
    for i in range(1, n + 1):
        if i == sum_of_divisors(i):
            if sum_of_divisors(i) == i:
                continue
            if sum_of_divisors(i) == sum_of_divisors(sum_of_divisors(i)):
                sum_ += i
    return sum_


def sum_of_divisors(n):
    """
    :param n: int
    :return: int
    """
    sum_ = 1
    for i in range(2, n):
        if n % i == 0:
            sum_ += i
    return sum_


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
    print(amicable_numbers_sum(1000000000000000000000000000))
    print(amicable_numbers_sum(10000000000000000000000000000))