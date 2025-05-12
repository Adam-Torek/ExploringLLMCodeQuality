"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(lst):
    """
    This function takes a list of numbers as an input and returns a new list of numbers
    that are the cubes of the original numbers.
    """
    # create an empty list to store the cubes
    new_lst = []
    # iterate over the list of numbers
    for num in lst:
        # cube the number and append it to the new list
        new_lst.append(num**3)
    # return the new list
    return new_lst

# test the function
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]