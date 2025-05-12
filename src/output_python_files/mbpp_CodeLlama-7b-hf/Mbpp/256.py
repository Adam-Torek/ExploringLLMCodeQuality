"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""


def count_Primes_nums(num):
    if num <= 1:
        return 0
    else:
        count = 0
        for i in range(2, num + 1):
            if is_prime(i):
                count += 1
        return count


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    print(count_Primes_nums(5))
    print(count_Primes_nums(10))
    print(count_Primes_nums(100))
    print(count_Primes_nums(1000))
    print(count_Primes_nums(10000))
    print(count_Primes_nums(100000))
    print(count_Primes_nums(1000000))
    print(count_Primes_nums(10000000))
    print(count_Primes_nums(100000000))
    print(count_Primes_nums(1000000000))
    print(count_Primes_nums(10000000000))
    print(count_Primes_nums(100000000000))
    print(count_Primes_nums(1000000000000))
    print(count_Primes_nums(10000000000000))
    print(count_Primes_nums(100000000000000))
    print(count_Primes_nums(1000000000000000))
    print(count_Primes_nums(10000000000000000))
    print(count_Primes_nums(100000000000000000))
    print(count_Primes_nums(1000000000000000000))
    print(count_Primes_nums(10000000000000000000))
    print(count_Primes_nums(100000000000000000000))
    print(count_Primes_nums(1000000000000000000000))
    print(count_Primes_nums(10000000000000000000000))
    print(count_Primes_nums(100000000000000000000000))
    print(count_Primes_nums(1000000000000000000000000))
    print(count_Primes_nums(10000000000000000000000000))
    print(count_Primes_nums(100000000000000000000000000))
    print(count_Primes_nums(1000000000000000000000000000))
    print(count_Primes_nums(1000000000000000000