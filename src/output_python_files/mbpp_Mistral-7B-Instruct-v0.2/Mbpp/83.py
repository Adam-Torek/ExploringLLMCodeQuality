"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_char(string):
    result = ""
    for char in string:
        ascii_val = ord(char) % 26
        result += chr(ascii_val + ord("a"))
    return result

# Test case
assert get_char("abc") == "f"
assert get_char("xyz") == "b"
assert get_char("pqr") == "u"
assert get_char("") == ""
assert get_char("z") == "z"
assert get_char("ABC") == "C"
assert get_char("123") == ""
assert get_char("Hello") == "J"