"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""

def odd_values_string(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 1])

# Test cases
assert odd_values_string('abcdef') == 'ace'
assert odd_values_string('hello') == 'hll'
assert odd_values_string('12345') == '12345'<|endoftext|>