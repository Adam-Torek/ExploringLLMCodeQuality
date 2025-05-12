"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    words = string.split()
    new_words = []
    for word in words:
        if len(word)!= k:
            new_words.append(word)
    return''.join(new_words)

# Test cases
assert remove_length('The person is most value tet', 3) == 'person is most value'
assert remove_length('The quick brown fox jumps over the lazy dog', 3) == 'quick brown fox jumps over lazy dog'
assert remove_length('The quick brown fox jumps over the lazy dog', 5) == 'The quick brown fox jumps over the lazy dog'<|endoftext|>