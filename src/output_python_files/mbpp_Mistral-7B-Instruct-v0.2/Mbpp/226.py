"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(string):
    """
    :param string: string to be processed
    :return: string with odd indexed characters removed
    """
    return ''.join([char for index, char in enumerate(string) if index % 2 != 0])

assert odd_values_string('abcdef') == 'ace'
assert odd_values_string('') == ''
assert odd_values_string('a') == 'a'
assert odd_values_string('hello') == 'h'