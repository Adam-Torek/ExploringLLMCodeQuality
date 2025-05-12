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
    vowels = 'aeiou'
    return sum(s.count(v) for v in vowels)

def count_consecutive_vowels(s: str) -> int:
    """ Return the number of consecutive vowels in a string.
    >>> count_consecutive_vowels('hello world')
    1
    >>> count_consecutive_vowels('aeiou')
    4
    >>> count_consecutive_vowels('')
    0
    """
    vowels = 'aeiou'
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

def count_pairs(s: str, p: str) -> int:
    """ Return the number of times a substring p appears as a pair in a string s.
    >>> count_pairs('abababc', 'ab')
    2
    >>> count_pairs('aabbcc', 'cd')
    0
    """
    return s.count(p) // 2

def count_substring_occurrences(s: str, p: str) -> int:
    """ Return the number of times a substring p appears in a string s.
    >>> count_substring_occurrences('abababc', 'ab')
    2
    >>> count_substring_occurrences('aabbcc', 'cd')
    0
    """
    return s.count(p)

def count_substring_pairs(s: str, p: str) -> int:
    """ Return the number of times a substring p appears as a pair in a string s.
    >>> count_substring_pairs('abababc', 'ab')
    2
    >>> count_substring_pairs('aabbcc', 'cd')
    0
    """
    return count_pairs(s, p)

def count_substring_triplets(s: str, p: str) -> int:
    """ Return the number of times a substring p appears as a triplet in a string s.
    >>> count_substring_triplets('