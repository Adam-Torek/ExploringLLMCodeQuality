"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please','move', 'back','stream'])
"""

def find_char_long(string):
    words = string.split()
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return result

# Test cases
assert set(find_char_long('Please move back to stream')) == set(['Please','move', 'back','stream'])
assert set(find_char_long('The quick brown fox jumps over the lazy dog')) == set(['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'])
assert set(find_char_long('')) == set([])<|endoftext|>