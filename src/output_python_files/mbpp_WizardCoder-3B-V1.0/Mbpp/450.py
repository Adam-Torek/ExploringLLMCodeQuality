"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice','solution'],8)==['practice','solution']
"""

def extract_string(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]<|endoftext|>