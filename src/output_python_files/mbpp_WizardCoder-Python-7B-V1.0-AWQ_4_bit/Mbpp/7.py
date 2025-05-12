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

print(find_char_long('Please move back to stream'))

# Output: {'Please', 'move', 'back', 'stream'}

# Test cases:
# assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
# assert set(find_char_long('Hello world')) == set(['Hello', 'world'])
# assert set(find_char_long('Python is awesome')) == set(['Python', 'awesome'])
# assert set(find_char_long('I am learning Python')) == set(['Python', 'learning']
# assert set(find_char_long('')) == set()
# assert set(find_char_long('a')) == set()
# assert set(find_char_long('a b c d e f g')) == set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# assert set(find_char_long('a b c d e f g h i j k l m n o p q r s t u v w x y z')) == set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# assert set(find_char_long('Aa bb cc dd ee ff gg hh ii jj kk ll mm nn op pp qq rr ss tt uu vv ww xx yy zz')) == set(['Aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'op', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
# assert set(find_char_long('1234567890')) == set()
# assert set(find_char_long('1234567890a') == set(['a'])
# assert set(find_char_long('1234567890a b c d e f g h i j k l m n o p q r s t u v w x y z') == set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char_long('Python is awesome') == set(['Python', 'awesome']
# assert set(find_char