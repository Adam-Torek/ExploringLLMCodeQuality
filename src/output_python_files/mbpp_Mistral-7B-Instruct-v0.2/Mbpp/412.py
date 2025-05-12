"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""
def remove_odd(numbers):
    """
    Function to remove odd numbers from a given list
    :param numbers: list of numbers
    :return: list without odd numbers
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

assert remove_odd([1,2,3]) == [2]
assert remove_odd([4,5,6]) == [4,6]
assert remove_odd([7,8,9]) == []
assert remove_odd([]) == []