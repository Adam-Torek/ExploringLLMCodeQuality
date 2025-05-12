"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(string):
    ascii_sum = 0
    for char in string:
        ascii_sum += ord(char)
    return chr((ascii_sum % 26) + ord('a'))

# Test the function
assert get_Char("abc") == "f"<|endoftext|>