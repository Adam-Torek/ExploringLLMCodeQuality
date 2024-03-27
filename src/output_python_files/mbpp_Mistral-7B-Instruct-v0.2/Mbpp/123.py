"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def divisor_sum(n):
    sum = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            sum += i + n//i
    return sum

def amicable_numbers_sum(n):
    amicable_numbers = []
    for i in range(1, n+1):
        if i != divisor_sum(i) and divisor_sum(divisor_sum(i)) == i:
            amicable_numbers.append(i)
    return sum(amicable_numbers)

assert amicable_numbers_sum(999) == 504</s>