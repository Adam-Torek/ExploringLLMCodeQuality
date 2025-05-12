"""
Write a function to extract values between quotation marks from a string.
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
"""
def extract_values(string):
    """
    Extracts values between quotation marks from a given string.

    :param string: The string from which values are to be extracted.
    :return: A list containing the extracted values.
    """
    return re.findall(r'"[^"]+"', string)

import re

assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']