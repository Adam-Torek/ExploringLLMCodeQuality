def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return True if string is palindrome, False otherwise
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    """
    return string == string[::-1]

def count_vowels(string: str) -> int:
    """ Count number of vowels in given string
    >>> count_vowels('hello')
    2
    >>> count_vowels('world')
    1
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

def count_consonants(string: str) -> int:
    """ Count number of consonants in given string
    >>> count_consonants('hello')
    3
    >>> count_consonants('world')
    4
    """
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0
    for char in string:
        if char not in vowels:
            count += 1
    return count

def count_chars(string: str, char: str) -> int:
    """ Count number of occurrences of given character in given string
    >>> count_chars('hello', 'l')
    1
    >>> count_chars('world', 'o')
    1
    """
    return string.count(char)

def count_words(string: str) -> int:
    """ Count number of words in given string
    >>> count_words('hello world')
    2
    >>> count_words('python is awesome')
    3
    """
    return len(string.split())

def reverse_string(string: str) -> str:
    """ Reverse given string
    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('world')
    'dlrow'
    """
    return string[::-1]

def remove_vowels(string: str) -> str:
    """ Remove all vowels from given string
    >>> remove_vowels('hello')
    'hll'
    >>> remove_vowels('world')
    'wrd'
    """
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in string if char not in vowels])

def remove_consonants(string: str) -> str:
    """ Remove all consonants from given string
    >>> remove_consonants('hello')
    'ee'
    >>> remove_consonants('world')
    'wwrr'
    """
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return ''.join([char for char in string if char not in consonants])

def remove_duplicates(string: str) -> str:
    """ Remove duplicates from given string
    >>> remove_duplicates('hello')
    'helo'
    >>> remove_duplicates('world')
    'worl'
    """
    return ''.join(sorted(set(string), key=string.index)

def is_anagram(string1: str, string2: str) -> bool:
    """ Return True if given strings are anagr