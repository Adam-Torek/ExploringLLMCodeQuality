"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def sum_amicable_numbers(n):
    amicable_numbers = []
    for i in range(1, n):
        if i == sum_of_divisors(i):
            amicable_numbers.append(i)
    return sum(amicable_numbers)

def sum_of_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def amicable_numbers_sum(n):
    return sum_amicable_numbers(n)

# Test the function
assert amicable_numbers_sum(999) == 504<|endoftext|>