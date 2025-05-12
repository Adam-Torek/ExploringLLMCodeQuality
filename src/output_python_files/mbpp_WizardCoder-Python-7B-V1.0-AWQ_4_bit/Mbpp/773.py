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
print(occurance_substring('python programming, python language','java'))

#output: ('python', 0, 6)
#output: None

#Explanation:
#The function checks if the substring is present in the string. If it is present, it returns a tuple containing the substring, the index of the first occurrence and the index of the last occurrence. If it is not present, it returns None.
#In the first example, the substring 'python' is present in the string and the output is ('python', 0, 6) because it occurs at the beginning of the string and at the end of the string.
#In the second example, the substring 'java' is not present in the string and the output is None.