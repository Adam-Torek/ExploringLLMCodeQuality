"""
Write a function that takes in two numbers and returns a tuple with the second number and then the first number.
assert swap_numbers(10,20)==(20,10)
"""
def swap_numbers(num1, num2):
    """
    Swaps the order of two numbers and returns a tuple with the swapped numbers
    :param num1: The first number
    :param num2: The second number
    :return: A tuple with the second number first and the first number second
    """
    return (num2, num1)

# Test the function
assert swap_numbers(10, 20) == (20, 10)
assert swap_numbers(3, 5) == (5, 3)
assert swap_numbers(1, 1) == (1, 1)