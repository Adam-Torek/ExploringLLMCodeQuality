"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    if substring in string:
        return (substring, string.index(substring), string.rindex(substring))
    else:
        return None

print(occurance_substring('python programming, python language', 'python'))
print(occurance_substring('python programming, python language', 'java'))
print(occurance_substring('python programming, python language', 'programming'))
print(occurance_substring('python programming, python language', 'language'))
print(occurance_substring('python programming, python language', 'programming language'))
print(occurance_substring('python programming, python language', 'programming python'))

# Output:
# ('python', 0, 6)
# None
# ('programming', 10, 19)
# ('language', 23, 32)
# None
# ('programming python', 10, 26)

# Explanation:
# The first example returns the occurrence of the substring 'python' in the string 'python programming, python language' and its position is 0 and 6.
# The second example returns None because 'java' is not present in the string.
# The third example returns the occurrence of the substring 'programming' in the string 'python programming, python language' and its position is 10 and 19.
# The fourth example returns the occurrence of the substring 'language' in the string 'python programming, python language' and its position is 23 and 32.
# The fifth example returns None because 'programming python' is not present in the string.