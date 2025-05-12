"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""

def replace_char(string, old_char, new_char):
    """
    This function takes in a string, an old character and a new character
    and returns the string with all occurrences of the old character replaced
    with the new character.
    """
    # split the string into a list of characters
    string_list = list(string)
    # iterate over the list of characters
    for i in range(len(string_list)):
        # if the current character is the old character
        if string_list[i] == old_char:
            # replace the character with the new character
            string_list[i] = new_char
    # join the list of characters back into a string
    return ''.join(string_list)

# test the function
assert replace_char("polygon",'y','l')==("pollgon")