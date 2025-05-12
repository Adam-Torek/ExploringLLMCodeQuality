"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""

def extract_rear(tup):
    return [s[-1] for s in tup]

print(extract_rear(('Mers', 'for', 'Vers' )) # Output: ['s', 'r', 's']