"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    words = string.split()
    result = []
    for word in words:
        if len(word)!= k:
            result.append(word)
    return''.join(result)

print(remove_length('The person is most value tet', 3))
<file_sep>/python/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000_python_basic/0000