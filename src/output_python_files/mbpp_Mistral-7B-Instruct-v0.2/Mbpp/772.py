"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
import re

def remove_length(string, k):
    pattern = r'\b\w{k}\b'
    return re.sub(pattern, '', string)

assert remove_length('The person is most value tet', 3) == 'person is most value'