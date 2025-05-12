def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''

def is_prime(number):
    '''
    Create a function that takes a number as an argument and returns
    True if the number is a prime number and False otherwise.

    Examples
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    '''

def is_palindrome(word):
    '''
    Create a function that takes a string as an argument and returns
    True if the string is a palindrome and False otherwise.

    Examples
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("tacocat")
    True
    >>> is_palindrome("palindrome")
    False
    '''

def is_anagram(word1, word2):
    '''
    Create a function that takes two strings as arguments and returns
    True if the strings are anagrams and False otherwise.

    Examples
    >>> is_anagram("cristian", "crisitna")
    True
    >>> is_anagram("cristian", "crisitna")
    True
    >>> is_anagram("cristian", "crisitna")
    True
    '''

def is_pangram(sentence):
    '''
    Create a function that takes a string as an argument and returns
    True if the string is a pangram and False otherwise.

    Examples
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    '''

def is_isogram(word):
    '''
    Create a function that takes a string as an argument and returns
    True if the string is an isogram and False otherwise.

    Examples
    >>> is_isogram("lumberjack")
    True
    >>> is_isogram("lumberjack")
    True
    >>> is_isogram("lumberjack")
    True
    '''

def is_vowel(letter):
    '''
    Create a function that takes a character as an argument and returns
    True if the character is a vowel and False otherwise.

    Examples
    >>> is_vowel("a")
    True
    >>> is_vowel("a")
    True
    >>> is_vowel("a")
    True
    '''

def is_consonant(letter):
    '''
    Create a function that takes a character as an argument and returns
    True if the character is a consonant and False otherwise.

    Examples
    >>> is_consonant("a")
    False
    >>> is_consonant("a")
    False
    >>> is_consonant("a")
    False
    '''

def is_punctuation(character):
    '''
    Create a function that takes a character as an argument and returns
    True if the character is a punctuation mark and False otherwise.

    Examples
    >>> is_punctuation("!")
    True
    >>> is_punctuation("!")
    True
    >>> is_punctuation("!")
    True
    '''

def is_whitespace(character):
    '''
    Create a function that takes a character as an argument and returns
    True if the character is a whitespace character and False otherwise.

    Examples
    >>> is_whitespace(" ")
    True
    >>> is_whitespace(" ")
    True
    >>> is_whitespace(" ")
    True
    '''

def is_uppercase(character):
    '''
    Create a function that takes a character as an argument and returns
    True if the character is uppercase and False otherwise.

    Examples
    >>> is_uppercase("A")
    True
    >>> is_uppercase("A")
    True
    >>> is_uppercase("A")
    True
    '''

def is_lowercase(character):
    '''
    Create a function that takes a character as an argument and returns
    True if the character is lowercase and False otherwise.

    Examples
    >>> is_lowercase("a