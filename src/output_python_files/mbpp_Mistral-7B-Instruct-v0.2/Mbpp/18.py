"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(string_to_clean, dirty_chars):
    """
    :param string_to_clean: string to clean
    :param dirty_chars: string with characters to remove
    :return: string with dirty chars removed
    """
    return ''.join([char for char in string_to_clean if char not in dirty_chars])

assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("python", "pyth") == 'on'
assert remove_dirty_chars("python", "pth") == 'yon'
assert remove_dirty_chars("python", "p") == 'hthon'
assert remove_dirty_chars("python", "") == 'python'