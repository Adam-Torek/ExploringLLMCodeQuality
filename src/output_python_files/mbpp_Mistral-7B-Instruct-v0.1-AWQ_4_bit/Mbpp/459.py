"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""

def remove_uppercase(string):
    """
    Remove uppercase substrings from a given string.
    """
    # split the string into a list of characters
    string_list = list(string)
    # iterate over the list of characters
    for i in range(len(string_list)):
        # check if the current character is uppercase
        if string_list[i].isupper():
            # remove the uppercase character from the list
            string_list.pop(i)
    # join the list of characters back into a string
    return ''.join(string_list)

# test the function
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'