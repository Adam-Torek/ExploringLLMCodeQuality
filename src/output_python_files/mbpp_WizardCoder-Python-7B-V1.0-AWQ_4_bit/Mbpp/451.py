"""
Write a function to remove all whitespaces from the given string.
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
"""

def remove_whitespaces(string):
    return ''.join(string.split())

# Test cases
print(remove_whitespaces(' Google    Flutter ')) # Output: 'GoogleFlutter'