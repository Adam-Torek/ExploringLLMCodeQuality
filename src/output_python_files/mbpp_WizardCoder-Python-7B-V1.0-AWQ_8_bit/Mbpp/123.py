"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def amicable_numbers_sum(n):
    def sum_divisors(num):
        return sum(d for d in range(1, num) if num % d == 0)

    def is_amicable(a, b):
        return sum_divisors(a) == b and sum_divisors(b) == a

    total = 0
    for i in range(1, n+1):
        if is_amicable(i, sum_divisors(i)):
            total += i
    return total

print(amicable_numbers_sum(999)) # 504