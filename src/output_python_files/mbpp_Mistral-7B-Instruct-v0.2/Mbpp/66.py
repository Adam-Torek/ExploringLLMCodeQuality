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
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

# Test the function
assert pos_count([1,-2,3,-4]) == 2
assert pos_count([-1, -2, -3, -4]) == 0
assert pos_count([0, 1, 2, 3]) == 4
assert pos_count([]) == 0
assert pos_count([1, 1, 1, 1]) == 4