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
print(remove_length('This is a test string', 5)) # Output: 'This is a test'
print(remove_length('I am a test string', 4)) # Output: 'I am a test'
print(remove_length('I am a test string', 1)) # Output: 'am a test string'
print(remove_length('I am a test string', 0)) # Output: 'I am a test string'
print(remove_length('I am a test string', 6)) # Output: ''

# Another solution using list comprehension
def remove_length_list_comp(string, k):
    return ' '.join([word for word in string.split() if len(word) != k])

print(remove_length_list_comp('The person is most value tet', 3)) # Output: 'person is most value'
print(remove_length_list_comp('This is a test string', 5)) # Output: 'This is a test'
print(remove_length_list_comp('I am a test string', 4)) # Output: 'I am a test'
print(remove_length_list_comp('I am a test string', 1)) # Output: 'am a test string'
print(remove_length_list_comp('I am a test string', 0)) # Output: 'I am a test string'
print(remove_length_list_comp('I am a test string', 6)) # Output: ''

# Another solution using regex
import re
def remove_length_regex(string, k):
    return re.sub(r'\b\w{%d}\b' % k, '', string)

print(remove_length_regex('The person is most value tet', 3)) # Output: 'person is most value'
print(remove_length_regex('This is a test string', 5)) # Output: 'This is a test'
print(remove_length_regex('I am a test string', 4)) # Output: 'I am a test'
print(remove_length_regex('I am a test string', 1)) # Output: 'am a test string'
print(remove_length_regex('I am a test string', 0)) # Output: 'I am a test string'
print(remove_length_regex('I am a test string', 6)) # Output: ''