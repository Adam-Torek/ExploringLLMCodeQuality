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
    This function is a test function to check if the find_even_numbers function is working correctly.

    :param numbers: list of numbers
    :return: list of even numbers
    """
    assert find_even_numbers([1,2,3,4,5]) == [2,4]
    return find_even_numbers(numbers)

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    print(find_even_numbers(numbers))