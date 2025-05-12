"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(string):
    """
    This function takes a string as an argument and returns a new string with all whitespaces removed.
    """
    return string.replace(" ", "")

# Test the function
assert remove_all_spaces('python  program') == 'pythonprogram'