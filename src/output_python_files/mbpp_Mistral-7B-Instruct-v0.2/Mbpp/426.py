"""
Write a function to filter odd numbers.
assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]
"""
def filter_oddnumbers(numbers):
    """
    Filter odd numbers from the given list
    :param numbers: list of numbers
    :return: list of odd numbers
    """
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]