"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
def remove_all_spaces(string):
    return string.replace(" ", "")

# Test cases
print(remove_all_spaces('python  program')) # Output: 'pythonprogram'