"""
Write a function to count the number of occurence of the string 'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""
def count_occurance(string):
    """
    :param string: string to search for the occurence of 'std'
    :return: int, number of occurence of 'std' in the given string
    """
    return string.count('std')