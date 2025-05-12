"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
def extract_nth_element(lst, n):
    """
    Extracts the nth element from a given list of tuples.

    Parameters:
    lst (list): A list of tuples.
    n (int): The index of the element to extract.

    Returns:
    The nth element from the given list of tuples.
    """
    if len(lst) <= n:
        raise IndexError("List index out of range")
    return lst[n][0]

# Test case
lst = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
assert extract_nth_element(lst, 0) == 'Greyson Fulton'
assert extract_nth_element(lst, 3) == 'Beau Turnbull'