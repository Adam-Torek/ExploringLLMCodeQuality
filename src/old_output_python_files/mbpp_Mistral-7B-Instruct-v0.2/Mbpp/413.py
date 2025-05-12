"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
def extract_nth_element(lst, n):
    """
    Extracts the nth element from a given list of tuples.

    Args:
        lst: A list of tuples.
        n: The index of the element to extract.

    Returns:
        The nth element from the given list of tuples.
    """
    return [i[n] for i in lst]

# Test case
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0) == ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']