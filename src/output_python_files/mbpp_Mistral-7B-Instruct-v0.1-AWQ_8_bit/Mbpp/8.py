"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(lst):
    """
    This function takes a list as an input and returns a new list with the squares of each element in the original list.
    """
    result = []
    for num in lst:
        result.append(num**2)
    return result

# test the function
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]