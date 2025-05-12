"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""

def dict_filter(dictionary: dict, n: int) -> dict:
    """
    Takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
    :param dictionary: The dictionary to filter
    :param n: The integer to filter by
    :return: The filtered dictionary
    """
    filtered_dictionary = {}
    for key, value in dictionary.items():
        if value >= n:
            filtered_dictionary[key] = value
    return filtered_dictionary