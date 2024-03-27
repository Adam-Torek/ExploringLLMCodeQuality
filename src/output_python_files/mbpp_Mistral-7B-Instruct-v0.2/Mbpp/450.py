"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(lst, size):
    """
    Extracts strings of given size from the list of strings
    :param lst: list of strings
    :param size: size of the strings to be extracted
    :return: list of extracted strings
    """
    extracted_strings = []
    for string in lst:
        if len(string) >= size:
            extracted_strings.append(string[:size])
    return extracted_strings

assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']</s>