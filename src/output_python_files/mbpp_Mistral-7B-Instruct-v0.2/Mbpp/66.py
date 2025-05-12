"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""
def pos_count(numbers):
    """
    Function to count the number of positive numbers in a list
    :param numbers: list of numbers
    :return: int, number of positive numbers in the list
    """
    return sum(1 for num in numbers if num > 0)

# Test the function
assert pos_count([1,-2,3,-4]) == 2
assert pos_count([-1,0,1,2]) == 3
assert pos_count([0,0,0]) == 0
assert pos_count([-1,-2,-3]) == 0