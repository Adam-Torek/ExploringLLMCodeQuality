"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(string1, string2):
    """
    :param string1: string to clean
    :param string2: string with characters to remove
    :return: string with removed characters
    """
    return ''.join([char for char in string1 if char not in string2])

assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("python", "py") == "thn"
assert remove_dirty_chars("", "abc") == ""
assert remove_dirty_chars("abc", "abc") == ""
assert remove_dirty_chars("abc", "xyz") == "abc"