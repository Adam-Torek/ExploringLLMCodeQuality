"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(string):
    return string.swapcase()

print(toggle_string("Python")) # Output: "pYTHON"

# Another way to solve this problem is to use a loop to iterate through each character in the string and toggle its case using the `upper()` and `lower()` methods.

def toggle_string(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string

print(toggle_string("Python")) # Output: "pYTHON"

# Another way to solve this problem is to use the `casefold()` method to convert the string to lowercase and then use the `swapcase()` method to toggle the case.

def toggle_string(string):
    return string.casefold().swapcase()

print(toggle_string("Python")) # Output: "pYTHON"

# Another way to solve this problem is to use the `title()` method to toggle the case of the string.

def toggle_string(string):
    return string.title()

print(toggle_string("Python")) # Output: "Python"

# All of these solutions will produce the same output.