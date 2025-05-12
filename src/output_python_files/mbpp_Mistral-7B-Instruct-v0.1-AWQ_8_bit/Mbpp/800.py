"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""

def remove_all_spaces(string):
    """
    This function removes all whitespaces from a given string.
    :param string: string
    :return: string without whitespaces
    """
    return ''.join(string.split())