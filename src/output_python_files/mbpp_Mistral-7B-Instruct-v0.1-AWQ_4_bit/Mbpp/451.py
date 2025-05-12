"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""

def remove_whitespaces(string):
    """
    This function removes all whitespaces from the given string.
    """
    return string.replace(" ", "")

# Test the function
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'