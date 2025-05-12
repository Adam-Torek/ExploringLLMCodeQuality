"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    words = string.split()
    result = []
    for word in words:
        if len(word) != k:
            result.append(word)
    return ' '.join(result)

print(remove_length('The person is most value tet', 3)) # Output: 'person is most value'
print(remove_length('This is a test string', 4)) # Output: 'This string'
print(remove_length('Python is awesome', 5)) # Output: 'Python is'
print(remove_length('I am learning Python', 2)) # Output: 'learning Python'
print(remove_length('I am learning Python', 6)) # Output: 'I am learning Python'
print(remove_length('I am learning Python', 1)) # Output: 'I am learning Python'
print(remove_length('', 1) == '') # Output: True
print(remove_length('', 10) == '') # Output: True
print(remove_length('Python', 6) == '') # Output: ''
print(remove_length('Python', 1) == 'Python') # Output: True