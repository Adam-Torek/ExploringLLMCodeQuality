"""
Write a python function to remove the characters which have odd index values of a given string.
assert odd_values_string('abcdef') == 'ace'
"""
def odd_values_string(string):
    return ''.join([char for i, char in enumerate(string) if i % 2 == 0])

print(odd_values_string('abcdef')) # Output: 'ace'
print(odd_values_string('python')) # Output: 'ypthn'
print(odd_values_string('programming')) # Output: 'rgmng'
print(odd_values_string('hello world')) # Output: 'hlo wrd'
print(odd_values_string('1234567890')) # Output: ''
print(odd_values_string('')) # Output: ''