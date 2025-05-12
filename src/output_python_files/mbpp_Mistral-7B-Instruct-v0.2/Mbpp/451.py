"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""
def remove_whitespaces(string):
    """
    :param string: string to remove whitespaces from
    :return: string without whitespaces
    """
    return string.replace(" ", "")

assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'