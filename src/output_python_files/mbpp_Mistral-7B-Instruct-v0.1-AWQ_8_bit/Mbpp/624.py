"""
Write a python function to convert a given string to uppercase.
assert is_upper("person") =="PERSON"
"""

def is_upper(string):
    """
    This function takes a string as an input and returns the string in uppercase.
    """
    return string.isupper()

# Test the function
assert is_upper("person") == "PERSON"