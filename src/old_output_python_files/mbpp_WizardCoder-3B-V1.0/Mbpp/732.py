"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""
def replace_specialchar(string):
    return string.replace(',', ':').replace('.', ':').replace(' ', ':')<|endoftext|>