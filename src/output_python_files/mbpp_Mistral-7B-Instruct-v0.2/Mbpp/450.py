"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(lst, size):
    """
    :param lst: list of strings
    :param size: size of the substring to extract
    :return: list of substrings of given size from the input list
    """
    return [lst[i][:size] for i in range(len(lst))]

assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']