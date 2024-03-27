"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(string):
    """
    :param string: string to remove spaces from
    :return: string without spaces
    """
    return string.replace(" ", "")

assert remove_all_spaces('python  program') == 'pythonprogram'</s>