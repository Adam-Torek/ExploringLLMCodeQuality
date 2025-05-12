"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(string):
    """
    :param string: string to remove whitespaces from
    :return: string with all whitespaces removed
    """
    return string.replace(" ", "")

# Test the function
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'