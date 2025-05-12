"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""

def remove_dirty_chars(string1, string2):
    """
    :param string1:
    :param string2:
    :return:
    """
    result = ""
    for char in string1:
        if char not in string2:
            result += char
    return result


# assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
# assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'