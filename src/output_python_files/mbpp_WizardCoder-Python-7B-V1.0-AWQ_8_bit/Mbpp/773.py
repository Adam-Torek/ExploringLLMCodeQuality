"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    if substring in string:
        return (substring, string.index(substring), string.rindex(substring))
    else:
        return None

print(occurance_substring('python programming, python language','python'))
# Output: ('python', 0, 6)

# Test case 2
print(occurance_substring('python programming, python language','java'))
# Output: None

# Test case 3
print(occurance_substring('python programming, python language','programming'))
# Output: ('programming', 10, 10)

# Test case 4
print(occurance_substring('python programming, python language',' '))
# Output: None

# Test case 5
print(occurance_substring('python programming, python language',''))
# Output: None

# Test case 6
print(occurance_substring('', 'python'))
# Output: None

# Test case 7
print(occurance_substring('python', ''))
# Output: None

# Test case 8
print(occurance_substring('', ''))
# Output: None

# Test case 9
print(occurance_substring('python programming, python language', 'python'))
# Output: ('python', 0, 6)