"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""

def occurance_substring(string, substring):
    """
    :param string: string to search
    :param substring: substring to search
    :return: tuple of (substring, position, length) or None if not found
    """
    if substring in string:
        start_index = string.index(substring)
        length = len(substring)
        return (substring, start_index, length)
    else:
        return None