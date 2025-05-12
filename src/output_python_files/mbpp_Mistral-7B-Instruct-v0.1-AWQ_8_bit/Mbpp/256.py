"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 0
    else:
        count = 0
        for i in range(2, n):
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                count += 1
        return count


if __name__ == '__main__':
    assert count_Primes_nums(5) == 2