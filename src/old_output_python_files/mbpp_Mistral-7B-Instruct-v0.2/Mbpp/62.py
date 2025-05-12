"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(numbers):
    """
    This function takes a list of numbers as an argument and returns the smallest number in the list.
    """
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Test the function
assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([-5, 0, 1, 45, 99]) == -5
assert smallest_num([1, 1, 1, 1]) == 1
assert smallest_num([]) is None
assert smallest_num([None, None, None]) is None