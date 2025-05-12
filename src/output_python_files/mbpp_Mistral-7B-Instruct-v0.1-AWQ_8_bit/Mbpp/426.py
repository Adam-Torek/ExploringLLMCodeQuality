"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""

def filter_oddnumbers(numbers):
    """
    This function filters odd numbers from the list.
    :param numbers: list of numbers
    :return: list of odd numbers
    """
    return [num for num in numbers if num % 2 != 0]

#assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]