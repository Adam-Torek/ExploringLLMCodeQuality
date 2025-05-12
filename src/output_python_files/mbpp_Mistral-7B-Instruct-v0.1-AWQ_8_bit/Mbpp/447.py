"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(lst):
    """
    This function takes a list of numbers as an input and returns a list of the cubes of the numbers in the list.
    """
    result = []
    for num in lst:
        result.append(num ** 3)
    return result

# test the function
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]