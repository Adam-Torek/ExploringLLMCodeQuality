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
    """ Return count of vowels in given string
    >>> count_vowels('hello')
    1
    >>> count_vowels('python')
    2
    """
    vowels = 'aeiou'
    return sum(1 for char in string.lower() if char in vowels)

def count_consonants(string: str) -> int:
    """ Return count of consonants in given string
    >>> count_consonants('hello')
    3
    >>> count_consonants('python')
    4
    """
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return sum(1 for char in string.lower() if char in consonants)

def count_chars(string: str) -> int:
    """ Return count of unique characters in given string
    >>> count_chars('hello')
    2
    >>> count_chars('python')
    6
    """
    return len(set(string.lower()) - set('aeiou')

def count_words(string: str) -> int:
    """ Return count of words in given string
    >>> count_words('hello world')
    2
    >>> count_words('python is awesome')
    3
    """
    return len(string.split())

def count_unique_words(string: str) -> int:
    """ Return count of unique words in given string
    >>> count_unique_words('hello world')
    1
    >>> count_unique_words('python is awesome')
    2
    """
    return len(set(string.split()))

def count_sentences(string: str) -> int:
    """ Return count of sentences in given string
    >>> count_sentences('Hello, world!')
    1
    >>> count_sentences('Python is awesome. It is fun.')
    2
    """
    return len(string.split('. '))

def count_punctuation(string: str) -> int:
    """ Return count of punctuation in given string
    >>> count_punctuation('Hello, world!')
    1
    >>> count_punctuation('Python is awesome. It is fun.')
    2
    """
    return sum(string.count(char) for char in '.,!?;:')

def count_uppercase(string: str) -> int:
    """ Return count of uppercase characters in given string
    >>> count_uppercase('Hello, world!')
    1
    >>> count_uppercase('Python is awesome. It is fun.')
    2
    """
    return sum(1 for char in string if char.isupper())

def count_lowercase(string: str) -> int:
    """ Return count of lowercase characters in given string
    >>> count_lowercase('Hello, world!')
    10
    >>> count_lowercase('Python is awesome. It is fun.')
    12
    """
    return sum(1 for char in string if char.islower())

def count_digits(string: str) -> int:
    """ Return count of digits in given string
    >>> count_digits('Hello, world!')
    0
    >>> count_digits('Python 3.8.2')
    2
    """
    return sum(1 for char in string if char.isdigit())

def count_spaces(string: str) -> int:
    """ Return count of spaces in given string
    >>> count_spaces('Hello, world!')
    1
    >>> count_spaces('Python is awesome. It is fun.')
    3
    """
    return sum(1 for char in string if char.isspace())

def count_vowels