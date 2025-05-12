"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(string):
    """
    Toggles the case of all characters in a string
    :param string: string
    :return: string
    """
    return string.swapcase()

assert toggle_string("Python") == "pYTHON"
assert toggle_string("python") == "Python"
assert toggle_string("") == ""
assert toggle_string("12345") == "12345"
assert toggle_string("Hello World") == "hELLO wORLD"
assert toggle_string("123aBc456") == "123aBc456"
assert toggle_string("123A bC 456") == "123a bC 456"
assert toggle_string("123A bC 456!") == "123a bC 456!"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n\r") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n\r"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n\r\f") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n\r\f"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n\r\f\v") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n\r\f\v"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n\r\f\v\b") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n\r\f\v\b"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n\r\f\v\b\n") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n\r\f\v\b\n"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/ \t\n\r\f\v\b\n\r") == "123a bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/\t\n\r\f\v\b\n\r"
assert toggle_string("123A bC 456! @#$%^&*()_+-=[]{}|;:,.<>?/