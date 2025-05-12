"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""
def remove_odd(numbers):
    """
    This function takes a list as an argument and returns a new list with all odd numbers removed.
    """
    return [num for num in numbers if num % 2 == 0]

# Test the function
assert remove_odd([1,2,3]) == [2]
assert remove_odd([4,5,6]) == [4,6]
assert remove_odd([]) == []
assert remove_odd([-1,0,1]) == [0]