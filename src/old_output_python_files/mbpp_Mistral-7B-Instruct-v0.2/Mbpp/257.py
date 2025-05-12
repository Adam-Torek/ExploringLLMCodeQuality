"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""
def swap_numbers(num1, num2):
    """
    Swaps the position of two numbers in a tuple
    :param num1: first number
    :param num2: second number
    :return: tuple with the second number first and the first number second
    """
    return (num2, num1)

assert swap_numbers(10,20)==(20,10)