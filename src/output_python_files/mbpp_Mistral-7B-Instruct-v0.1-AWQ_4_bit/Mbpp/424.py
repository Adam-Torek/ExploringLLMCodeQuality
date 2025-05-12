"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""

def extract_rear(tuple_list):
    """
    Extract only the rear index element of each string in the given tuple.
    """
    return [string[-1] for string in tuple_list]