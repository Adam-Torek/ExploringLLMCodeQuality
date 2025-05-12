"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""
from math import sqrt

def are_equivalent(num1, num2):
    """
    Determines if the sum of divisors of two integers are equal.
    """
    divisors_sum_num1 = sum(divisors(num1))
    divisors_sum_num2 = sum(divisors(num2))
    return divisors_sum_num1 == divisors_sum_num2

def divisors(num):
    """
    Returns a list of divisors of a given number.
    """
    divisors = [1]
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(int(num/i))
    return divisors

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum of divisors of {num1} is {sum(divisors(num1))} and the sum of divisors of {num2} is {sum(divisors(num2))}. Are they equivalent? {are_equivalent(num1, num2)}")