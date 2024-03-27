"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""

def occurance_substring(string, substring):
    """
    Find the occurrence and position of the substrings within a string.
    Return None if there is no match.
    """
    index = string.find(substring)
    if index == -1:
        return None
    else:
        return substring, index, index + len(substring)

# Test the function
print(occurance_substring('python programming, python language','python')) # ('python', 0, 6)<|endoftext|>