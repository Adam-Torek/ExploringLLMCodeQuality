"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""

def replace_specialchar(text):
    """
    Replace all occurrences of spaces, commas, or dots with a colon.
    """
    text = text.replace(" ", ":").replace(",", ":").replace(".", ":")
    return text


if __name__ == '__main__':
    assert replace_specialchar('Python language, Programming language.') == ('Python:language::Programming:language:')