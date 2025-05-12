"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
def neg_nos(numbers):
    """
    This function takes a list of numbers as an argument and returns a new list containing only the negative numbers.

    :param numbers: list of numbers
    :return: list of negative numbers
    """
    negative_numbers = [num for num in numbers if num < 0]
    return negative_numbers

if __name__ == "__main__":
    assert neg_nos([-1,4,5,-6]) == [-1,-6]
    print("Test passed!")