"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

def extract_nth_element(lst, n):
    """
    This function takes in a list of tuples and an integer n as input.
    It returns the nth element of the list of tuples.
    """
    if n < 0:
        return "Invalid input. n must be a non-negative integer."
    elif n == 0:
        return lst
    else:
        return lst[n-1]