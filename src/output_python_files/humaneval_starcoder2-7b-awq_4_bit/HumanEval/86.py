def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """

def is_palindrome(s):
    """
    Write a function that takes a string and returns True if the string is a
    palindrome, False otherwise.
    A palindrome is a word, phrase, or sequence that reads the same backward as
    forward, e.g., madam or nurses run.
    Note: You should ignore case and spaces.

    For example:
    is_palindrome('madam') returns True
    is_palindrome('nurses run') returns True
    is_palindrome('hello') returns False
    """

def is_anagram(s1, s2):
    """
    Write a function that takes two strings and returns True if they are anagrams,
    False otherwise.
    An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.
    Note: You should ignore case and spaces.

    For example:
    is_anagram('hello', 'olleh') returns True
    is_anagram('hello', 'olle') returns False
    is_anagram('hello', 'hello') returns False
    """

def is_pangram(s):
    """
    Write a function that takes a string and returns True if it is a pangram,
    False otherwise.
    A pangram is a sentence that contains all the letters of the English
    alphabet at least once.
    Note: You should ignore case and spaces.

    For example:
    is_pangram('The quick brown fox jumps over the lazy dog') returns True
    is_pangram('The quick brown fox jumps over the lazy dog') returns False
    is_pangram('The quick brown fox jumps over the lazy dog') returns False
    """

def is_isogram(s):
    """
    Write a function that takes a string and returns True if it is an isogram,
    False otherwise.
    An isogram is a word or phrase without a repeating letter, e.g.,
    moose or live.
    Note: You should ignore case and spaces.

    For example:
    is_isogram('moose') returns True
    is_isogram('live') returns False
    is_isogram('live') returns False
    """

def is_prime(n):
    """
    Write a function that takes a positive integer and returns True if it is a
    prime number, False otherwise.
    A prime number is a positive integer that is divisible only by 1 and itself.
    Note: You should ignore case and spaces.

    For example:
    is_prime(1) returns False
    is_prime(2) returns True
    is_prime(3) returns True
    is_prime(4) returns False
    is_prime(5) returns True
    is_prime(6) returns False
    is_prime(7) returns True
    is_prime(8) returns False
    is_prime(9) returns False
    is_prime(10) returns False
    """

def is_perfect(n):
    """
    Write a function that takes a positive integer and returns True if it is a
    perfect number, False otherwise.
    A perfect number is a positive integer that is equal to the sum of its
    positive divisors, excluding the number itself.
    Note: You should ignore case and spaces.

    For example:
    is_perfect(1) returns False
    is_perfect(2) returns False
    is_perfect(3) returns False
    is_perfect(4) returns True
    is_perfect(5) returns False
    is