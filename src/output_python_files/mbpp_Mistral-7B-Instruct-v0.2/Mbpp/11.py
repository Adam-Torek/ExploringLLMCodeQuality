"""
Write a python function to remove first and last occurrence of a given character from the string.
assert remove_Occ("hello","l") == "heo"
"""
def remove_Occ(string, char):
    """
    Function to remove first and last occurrence of a given character from the string
    :param string: string
    :param char: character to be removed
    :return: string without first and last occurrence of the given character
    """
    return string[::] [:string.index(char) if string.index(char) > 0 else 0] + string[::] [::-1].index(char) if string.rindex(char) > 0 else "" : string[::]

assert remove_Occ("hello","l") == "heo"
assert remove_Occ("python","p") == "ython"
assert remove_Occ("python","y") == "python"
assert remove_Occ("python","t") == "pyhon"
assert remove_Occ("python","h") == "pyon"