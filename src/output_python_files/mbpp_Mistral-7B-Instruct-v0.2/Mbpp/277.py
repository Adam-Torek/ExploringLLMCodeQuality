"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""
def dict_filter(dictionary, n):
    """
    :param dictionary: a dictionary
    :param n: an integer
    :return: a new dictionary with only the entries whose values are greater than or equal to n
    """
    filtered_dict = {}
    for key, value in dictionary.items():
        if value >= n:
            filtered_dict[key] = value
    return filtered_dict

# Test case
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},181)=={'Pierre Cox': 190}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},165)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
assert dict_filter({},170)=={}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},-1)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}