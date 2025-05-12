"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(string):
    """
    This function checks whether all the characters in the given string are same or not.
    :param string: string
    :return: boolean
    """
    if len(string) > 1:
        first_char = string[0]
        return all(char == first_char for char in string[1:])
    else:
        return True

assert all_Characters_Same("python") == False
assert all_Characters_Same("a") == True
assert all_Characters_Same("aaa") == True