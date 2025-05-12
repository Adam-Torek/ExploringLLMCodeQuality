"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
def remove_length(string, k):
    words = string.split()
    filtered_words = [word for word in words if len(word) != k]
    return ' '.join(filtered_words)

# Test case
assert remove_length('The person is most value tet', 3) == 'person is most value'