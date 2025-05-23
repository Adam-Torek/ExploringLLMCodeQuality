"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""
def replace_specialchar(string):
    """
    Replace all occurrences of spaces, commas, or dots with a colon in the given string.

    :param string: The string to be modified.
    :return: The modified string with all occurrences of spaces, commas, or dots replaced by colons.
    """
    return string.replace(" ", ":").replace(",", ":").replace(".", ":")

# Test the function
assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'