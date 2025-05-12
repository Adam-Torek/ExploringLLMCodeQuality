"""
Write a python function to find even numbers from a list of numbers.
assert Split([1,2,3,4,5]) == [2,4]
"""
def find_even_numbers(numbers):
    """
    This function takes a list of numbers as an argument and returns a new list containing only the even numbers.

    :param numbers: list of numbers
    :return: list of even numbers
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def Split(numbers):
    """
    This function checks if the given function 'find_even_numbers' returns the expected result for the given input.

    :param numbers: list of numbers
    :return: None
    """
    assert find_even_numbers([1,2,3,4,5]) == [2,4]

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    even_numbers = find_even_numbers(numbers)
    print(even_numbers)
    Split(numbers)