"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(lst):
    """
    This function takes a list of numbers as an input and returns a new list of the squares of the numbers in the original list.
    """
    # create an empty list to store the squares
    squares = []
    # iterate over the list of numbers
    for num in lst:
        # append the square of the current number to the list of squares
        squares.append(num**2)
    # return the list of squares
    return squares

# test the function with the given input
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]