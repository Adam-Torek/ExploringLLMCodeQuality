def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(i) for i in range(n+1))


def count_words(s: str) -> int:
    """ Return the number of words in a string.
    >>> count_words('hello world')
    1
    >>> count_words('a b c d e')
    4
    >>> count_words('')
    0
    """
    return len(s.split())

def count_unique_words(s: str) -> int:
    """ Return the number of unique words in a string.
    >>> count_unique_words('hello world')
    1
    >>> count_unique_words('a b c d e')
    4
    >>> count_unique_words('a b a b c d e')
    4
    """
    return len(set(s.split()))

def count_vowels(s: str) -> int:
    """ Return the number of vowels in a string.
    >>> count_vowels('hello world')
    2
    >>> count_vowels('aeiou')
    5
    >>> count_vowels('')
    0
    """
    vowels = set('aeiou')
    return sum(1 for c in s if c in vowels)

def count_consecutive_vowels(s: str) -> int:
    """ Return the number of consecutive vowels in a string.
    >>> count_consecutive_vowels('hello world')
    1
    >>> count_consecutive_vowels('aeiou')
    4
    >>> count_consecutive_vowels('')
    0
    """
    vowels = set('aeiou')
    count = 0
    for i in range(len(s)):
        if s[i] in vowels and (i == len(s) - 1 or s[i+1] not in vowels):
            count += 1
    return count

def count_uppercase_words(s: str) -> int:
    """ Return the number of words in a string that contain at least one uppercase letter.
    >>> count_uppercase_words('Hello world')
    1
    >>> count_uppercase_words('Aeiou')
    2
    >>> count_uppercase_words('')
    0
    """
    return sum(1 for word in s.split() if any(c.isupper() for c in word))

def count_punctuation(s: str) -> int:
    """ Return the number of punctuation characters in a string.
    >>> count_punctuation('hello, world!')
    2
    >>> count_punctuation('')
    0
    """
    return sum(1 for c in s if c in '.,;:?!')

def count_vowels_and_consecutive_vowels(s: str) -> str:
    """ Return a string containing the number of vowels and consecutive vowels in a string.
    >>> count_vowels_and_consecutive_vowels('hello world')
    'vowels: 2, consecutive vowels: 1'
    >>> count_vowels_and_consecutive_vowels('aeiou')
    'vowels: 5, consecutive vowels: 4'
    """
    vowels = set('aeiou')
    count_v = count_vowels(s)
    count_cv = count_consecutive_vowels(s)
    return f'vowels: {count_v}, consecutive vowels: {count_cv}'

def count_words_and_unique_words(s: str) -> str:
    """ Return a string containing the number of words and unique words in a string.
    >>> count_words_and_unique_words('hello world')
    'words: 2, unique words: 1'
    >>> count_words_