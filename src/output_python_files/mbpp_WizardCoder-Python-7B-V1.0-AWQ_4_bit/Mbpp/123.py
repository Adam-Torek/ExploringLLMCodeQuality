"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def amicable_numbers_sum(n):
    """
    Returns the sum of all amicable numbers from 1 to n.
    """
    def sum_divisors(num):
        """
        Returns the sum of all divisors of a number.
        """
        sum_div = 0
        for i in range(1, num):
            if num % i == 0:
                sum_div += i
        return sum_div

    def is_amicable(num):
        """
        Returns True if a number is amicable, False otherwise.
        """
        return sum_divisors(num) == num and sum_divisors(sum_divisors(num)) == num

    total = 0
    for i in range(1, n+1):
        if is_amicable(i):
            total += i
    return total

print(amicable_numbers_sum(999)) # 504