"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""
def first_odd(numbers):
    """
    This function takes a list of numbers as an argument and returns the first odd number in the list.
    If the list is empty, it raises a ValueError with the message "List cannot be empty".
    If the list contains no odd numbers, it returns None.
    """
    if not numbers:
        raise ValueError("List cannot be empty")

    for number in numbers:
        if number % 2 != 0:
            return number

    return None</s>