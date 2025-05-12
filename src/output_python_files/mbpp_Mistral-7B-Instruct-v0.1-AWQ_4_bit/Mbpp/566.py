"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


if __name__ == '__main__':
    print(sum_digits(345))