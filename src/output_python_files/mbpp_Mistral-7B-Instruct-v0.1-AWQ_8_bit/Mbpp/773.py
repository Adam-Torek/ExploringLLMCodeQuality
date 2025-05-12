"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""

def occurance_substring(string, substring):
    """
    :param string: string to search
    :param substring: substring to search
    :return: tuple of substring and its position in string
    """
    if substring in string:
        return substring, string.index(substring)
    else:
        return None


# assert occurance_substring('python programming, python language','python')==('python', 0, 6)
# assert occurance_substring('python programming, python language','python')==('python', 0, 6)
# assert occurance_substring('python programming, python language','python')==('python', 0, 6)