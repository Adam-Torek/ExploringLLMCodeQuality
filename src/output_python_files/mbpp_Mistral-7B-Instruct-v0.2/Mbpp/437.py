"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    """
    Function to remove odd characters in a string
    :param string: string
    :return: string without odd characters
    """
    return ''.join(filter(lambda x: ord(x) % 2 == 0, string))

assert remove_odd("python") == "yhn"
assert remove_odd("hello") == "l"
assert remove_odd("12345") == ""
assert remove_odd("") == ""
assert remove_odd("abcd") == "d"</s>