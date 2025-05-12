"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""

def toggle_string(string):
    """
    Toggle the case of all characters in a string
    :param string: string
    :return: string
    """
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string


#assert toggle_string("Python")==("pYTHON")
#print(toggle_string("Python"))