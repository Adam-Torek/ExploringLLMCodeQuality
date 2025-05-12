"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(tupl):
    return [i[-1] for i in tupl]

assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']