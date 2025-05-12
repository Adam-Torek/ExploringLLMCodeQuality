"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(input_string):
    """
    This function takes a string as an argument and returns a new string with all characters at odd index positions removed.
    :param input_string: string
    :return: string
    """
    output_string = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            output_string += char
    return output_string

assert odd_values_string('abcdef') == 'ace'