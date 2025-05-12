"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
def extract_nth_element(lst, n):
    """
    Extracts the nth element from a list of tuples.
    :param lst: list of tuples
    :param n: the nth element to extract
    :return: the nth element
    """
    if n < 0:
        return "Invalid input. n must be a positive integer."
    elif n == 0:
        return lst
    else:
        return lst[n-1]