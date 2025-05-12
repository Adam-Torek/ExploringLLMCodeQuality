"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""

def check_char(string):
    if string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"

print(check_char("abba")) # Output: Valid
print(check_char("hello")) # Output: Invalid
print(check_char("world")) # Output: Invalid
print(check_char("python")) # Output: Invalid
print(check_char("racecar")) # Output: Valid
print(check_char("go")) # Output: Invalid
print(check_char("goog")) # Output: Valid