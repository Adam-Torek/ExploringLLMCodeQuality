"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""


def swap_numbers(num1, num2):
    return (num2, num1)


print(swap_numbers(10, 20))