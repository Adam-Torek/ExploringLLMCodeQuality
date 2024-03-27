"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    start_index = 0
    while True:
        start_index = string.find(substring, start_index)
        if start_index == -1:
            return None
        yield substring, start_index, len(substring) + start_index
        start_index += len(substring)

# Test the function
assert list(occurance_substring('python programming, python language','python')) == [('python', 0, 6), ('python', 13, 20)]
assert list(occurance_substring('python programming, python language','java')) == []
assert list(occurance_substring('python programming, python language','python ')) == [('python', 0, 6), ('python', 23, 29)]</s>