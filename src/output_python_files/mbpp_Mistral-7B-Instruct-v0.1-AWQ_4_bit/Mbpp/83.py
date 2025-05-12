"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""

def get_Char(s: str) -> str:
    result = ""
    for char in s:
        result += chr((ord(char) % 26) + 97)
    return result


# test

print(get_Char("abc"))
print(get_Char("def"))
print(get_Char("ghi"))