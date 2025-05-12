"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""

def filter_oddnumbers(numbers):
    """
    This function filters out the even numbers from the list of numbers.
    :param numbers: list of numbers
    :return: list of odd numbers
    """
    # Using a list comprehension to filter out the even numbers
    return [number for number in numbers if number % 2 != 0]

# Testing the function
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]