"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(string, pattern):
    matches = re.findall(pattern, string)
    if matches:
        return matches[0], 0, len(matches[0])
    else:
        return None, None, None<|endoftext|>