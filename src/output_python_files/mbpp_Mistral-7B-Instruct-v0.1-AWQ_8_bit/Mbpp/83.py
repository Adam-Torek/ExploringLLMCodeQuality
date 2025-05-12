"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""

def get_Char(s: str) -> str:
    result = ""
    for i in range(len(s)):
        result += chr((ord(s[i]) - 97 + 26) % 26 + 97)
    return result