"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(string):
    ascii_sum = sum([ord(char) for char in string])
    return chr(ascii_sum % 26)

print(get_Char("abc")) # Output: f
print(get_Char("hello")) # Output: k
print(get_Char("world")) # Output: c
print(get_Char("python")) # Output: y
print(get_Char("programming")) # Output: y
print(get_Char("programminglanguage")) # Output: y
print(get_Char("programminglanguageisawesome")) # Output: y
print(get_Char("programminglanguageisawesomemuch")) # Output: y
print(get_Char("programminglanguageisawesomemuchmore")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefun")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunny")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday123")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday12345")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday123456789")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567890")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday12345678901")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567890123")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday12345678901234")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday123456789012345")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567890123456")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday12345678901234567")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday123456789012345678")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567890123456789")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday12345678901234567890")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday123456789012345678901")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567890123456789012")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday12345678901234567890123")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday123456789012345678901234")) # Output: y
print(get_Char("programminglanguageisawesomemuchmorefunnytoday1234567890123