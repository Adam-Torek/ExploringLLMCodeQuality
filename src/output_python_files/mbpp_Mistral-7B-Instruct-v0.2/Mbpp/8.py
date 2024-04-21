"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
def square_nums(numbers):
    """
    Function to find squares of individual elements in a list
    :param numbers: list of numbers
    :return: list of squares of individual numbers
    """
    return [num ** 2 for num in numbers]

# Test the function
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]</s>