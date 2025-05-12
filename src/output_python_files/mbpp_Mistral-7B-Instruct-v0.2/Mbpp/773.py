"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    """
    :param string: string to search for substring
    :param substring: substring to search for
    :return: tuple of substring and its position in the string
    """
    start_index = string.find(substring)
    if start_index == -1:
        return None
    else:
        return (substring, start_index, start_index + len(substring))

assert occurance_substring('python programming, python language','python')==('python', 0, 6)
assert occurance_substring('python programming, python language','java') is None
assert occurance_substring('python programming, python language, python','python')==('python', 0, 6)
assert occurance_substring('python programming, python language, python','java') is None
assert occurance_substring('python programming, python language, python','python')==('python', 12, 18)
assert occurance_substring('python programming, python language, python','python')==('python', 24, 30)