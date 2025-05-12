"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""
def check_char(s):
    if s[0] == s[-1]:
        return "Valid"
    else:
        return "Invalid"

# Test cases
print(check_char("abba")) # Valid
print(check_char("abc")) # Invalid<|endoftext|>