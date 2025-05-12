"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(string):
    return ''.join(filter(str.isupper, string))

# Test the function
assert remove_lowercase("PYTHon") == "PYTH"<|endoftext|>