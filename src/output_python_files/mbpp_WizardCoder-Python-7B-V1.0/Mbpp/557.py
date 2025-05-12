"""
Write a function to toggle the case of all characters in a string.
assert toggle_string("Python")==("pYTHON")
"""
def toggle_string(string):
    return string.swapcase()

# Test cases
print(toggle_string("Python")) # Output: pYTHON
print(toggle_string("Hello, World!")) # Output: hELLO, wORLD!
print(toggle_string("")) # Output: