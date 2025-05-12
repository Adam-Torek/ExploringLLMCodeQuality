"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""

def split(string):
    """
    This function takes a string as an input and returns a list of characters.
    """
    # split the string using split() method
    result = string.split()
    # return the result
    return result

# Test the function
assert split('python') == ['p','y','t','h','o','n']