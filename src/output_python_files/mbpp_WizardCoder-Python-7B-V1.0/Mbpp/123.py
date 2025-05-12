"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def amicable_numbers_sum(n):
    def sum_divisors(num):
        return sum(i for i in range(1, num) if num%i==0)

    def amicable(num1, num2):
        return sum_divisors(num1)==num2 and sum_divisors(num2)==num1

    total = 0
    for i in range(1, n+1):
        if amicable(i, sum_divisors(i)):
            total += i
    return total

print(amicable_numbers_sum(999)) # 504
print(amicable_numbers_sum(100000)) # 33378