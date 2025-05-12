"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""

def remove_dirty_chars(str1, str2):
    for char in str2:
        str1 = str1.replace(char, '')
    return str1

print(remove_dirty_chars("probasscurve", "pros")) # Output: 'bacuve'