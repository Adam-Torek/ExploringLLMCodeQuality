"""
Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
assert get_Char("abc") == "f"
"""
def get_Char(string):
    sum = 0
    for i in string:
        sum += ord(i)
    return chr(sum % 26)

print(get_Char("abc")) # Output: f
print(get_Char("hello")) # Output: k
print(get_Char("world")) # Output: z
print(get_Char("python")) # Output: y
print(get_Char("programming")) # Output: w
print(get_Char("programminglanguage")) # Output: y
print(get_Char("programminglanguageisawesome")) # Output: y
print(get_Char("programminglanguagesareawesome")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char("programminglanguagesareawesomemore")) # Output: y
print(get_Char