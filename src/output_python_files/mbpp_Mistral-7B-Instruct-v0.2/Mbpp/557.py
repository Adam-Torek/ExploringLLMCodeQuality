"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(string):
    """
    Toggles the case of all characters in a string
    :param string: str
    :return: str
    """
    return string.swapcase()

assert toggle_string("Python") == "pYTHON"
assert toggle_string("python") == "Python"
assert toggle_string("") == ""
assert toggle_string("Hello World") == "hELLO wORLD"</s>