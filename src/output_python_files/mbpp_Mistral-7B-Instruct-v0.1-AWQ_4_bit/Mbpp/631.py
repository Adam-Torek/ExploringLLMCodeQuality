"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""

def replace_spaces(string):
    """
    Function to replace whitespaces with an underscore and vice versa in a given string.
    """
    # split the string into a list of characters
    string_list = list(string)

    # iterate over the list of characters
    for i in range(len(string_list)):
        # check if the current character is a whitespace
        if string_list[i] == ' ':
            # replace the whitespace with an underscore
            string_list[i] = '_'
        elif string_list[i] == '_':
            # replace the underscore with a whitespace
            string_list[i] = ' '

    # join the list of characters back into a string
    new_string = ''.join(string_list)

    # return the new string
    return new_string

# test the function
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'