"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""

def extract_rear(strings):
    return [string[-1] for string in strings]

# Test cases
print(extract_rear(('Mers', 'for', 'Vers')) # Output: ['s', 'r', 's']
print(extract_rear(('Hello', 'World', 'Python')) # Output: ['o', 'd', 'n']
print(extract_rear(('A', 'B', 'C')) # Output: ['', ' ', '']