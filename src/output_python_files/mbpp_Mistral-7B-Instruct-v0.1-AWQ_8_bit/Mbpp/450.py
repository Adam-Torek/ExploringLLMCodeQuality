"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""

def extract_string(lst, size):
    """
    :param lst: list of string values
    :param size: size of string to extract
    :return: list of extracted string
    """
    extracted_list = []
    for string in lst:
        if len(string) >= size:
            extracted_list.append(string[:size])
    return extracted_list

#assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']