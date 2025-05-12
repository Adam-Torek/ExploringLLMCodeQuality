"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(string):
    """
    :param string: string to check
    :return: boolean value
    """
    if len(string) > 1:
        return all(char == string[0] for char in string[1:])
    else:
        return True

assert all_Characters_Same("python") == False
assert all_Characters_Same("a") == True
assert all_Characters_Same("aa") == True
assert all_Characters_Same("pythonpython") == True