"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(tuple_str):
    return [i[-1] for i in tuple_str]

# Testing the function
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
assert extract_rear(('apple', 'banana', 'cherry')) == ['e', 'a', 'y']
assert extract_rear(('cat', 'dog', 'elephant')) == ['t', 'g', 'p']</s>