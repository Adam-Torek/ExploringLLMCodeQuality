"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""
def odd_numbers(numbers):
    """
    :param numbers: list of integers
    :return: list of odd integers
    """
    return list(filter(lambda x: x % 2 != 0, numbers))

assert odd_numbers([1,2,3,4,5,6]) == [1,3,5]</s>