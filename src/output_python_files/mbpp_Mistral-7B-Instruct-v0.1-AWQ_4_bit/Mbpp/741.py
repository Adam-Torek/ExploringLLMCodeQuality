"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(string):
    """
    :param string: string
    :return: True if all characters are same, False otherwise
    """
    if len(string) > 1:
        return string[0] == string[1:]
    else:
        return True

# assert all_Characters_Same("python") == False
# assert all_Characters_Same("hello") == False
# assert all_Characters_Same("world") == True