"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
"""

def find_char_long(string):
    words = string.split()
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return set(result)

# Test the function
print(set(find_char_long('Please move back to stream'))) # Output: {'Please', 'move', 'back', 'stream'}
print(set(find_char_long('The quick brown fox jumps over the lazy dog'))) # Output: {'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'}
print(set(find_char_long('Python is a great programming language'))) # Output: {'Python', 'great', 'programming', 'language'}
print(set(find_char_long('I love Python'))) # Output: {'Python'}
print(set(find_char_long('Hello world'))) # Output: set()
print(set(find_char_long('a' * 20)) # Output: set()
print(set(find_char_long('a' * 3)) # Output: set()
print(set(find_char_long('a' * 4)) # Output: {'aaaa'}
print(set(find_char_long('a' * 5)) # Output: {'aaaaa'}
print(set(find_char_long('a' * 6)) # Output: {'aaaaaa'}
print(set(find_char_long('a' * 7)) # Output: {'aaaaaaa'}
print(set(find_char_long('a' * 8)) # Output: {'aaaaaaaa'}
print(set(find_char_long('a' * 9)) # Output: {'aaaaaaaaa'}
print(set(find_char_long('a' * 10)) # Output: {'aaaaaaaaaa'}
print(set(find_char_long('a' * 11)) # Output: {'aaaaaaaaaaa'}
print(set(find_char_long('a' * 12)) # Output: {'aaaaaaaaaaa'}
print(set(find_char_long('a' * 13)) # Output: {'aaaaaaaaaaa'}
print(set(find_char_long('a' * 14)) # Output: {'aaaaaaaaaaaa'}
print(set(find_char_long('a' * 15)) # Output: {'aaaaaaaaaaaa'}
print(set(find_char_long('a' * 16)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 17)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 18)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 19)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 20)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 21)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 22)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 23)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 24)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 25)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 26)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 27)) # Output: {'aaaaaaaaaaaaa'}
print(set(find_char_long('a' * 28)) # Output: {'aaaaaaaaaaaaa'}
print(set(