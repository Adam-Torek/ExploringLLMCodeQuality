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
    A palindrome is a string that is the same when reversed.

    For example:
    is_palindrome('abba') returns True
    is_palindrome('abbc') returns False
    is_palindrome('abcba') returns True
    is_palindrome('abccba') returns True
    is_palindrome('abccab') returns False
    """

def is_anagram(s1, s2):
    """
    Write a function that takes two strings and returns True if they are anagrams,
    False otherwise.
    An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.

    For example:
    is_anagram('abba', 'aabb') returns True
    is_anagram('abba', 'abab') returns False
    is_anagram('abba', 'abba') returns True
    is_anagram('abba', 'abbc') returns False
    is_anagram('abba', 'abbba') returns False
    """

def is_pangram(s):
    """
    Write a function that takes a string and returns True if it is a pangram,
    False otherwise.
    A pangram is a sentence that contains all the letters of the English
    alphabet at least once.

    For example:
    is_pangram('The quick brown fox jumps over the lazy dog') returns True
    is_pangram('The quick brown fox jumps over the dog') returns False
    is_pangram('The quick brown fox jumps over the lazy lazy dog') returns False
    """

def is_isogram(s):
    """
    Write a function that takes a string and returns True if it is an isogram,
    False otherwise.
    An isogram is a word or phrase without a repeating letter.

    For example:
    is_isogram('abba') returns False
    is_isogram('abbc') returns True
    is_isogram('abcba') returns False
    is_isogram('abccba') returns True
    is_isogram('abccab') returns False
    """

def is_prime(n):
    """
    Write a function that takes a number and returns True if it is a prime,
    False otherwise.
    A prime number is a number that is only divisible by itself and 1.

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
    Write a function that takes a number and returns True if it is a perfect
    number, False otherwise.
    A perfect number is a number that is equal to the sum of its factors.
    A factor of a number is a number that divides evenly into another number.

    For example:
    is_perfect(6) returns True
    is_perfect(7) returns False
    is_perfect(8) returns False
    is_perfect(9) returns True
    is_perfect(10) returns False
    is_perfect(11) returns False
    is_perfect(12) returns False
    is_perfect(13) returns False
    is_perfect(14) returns False
    is_perfect(15) returns False
    """

def is_armstrong(n):
    """
    Write a function that takes a number and returns True if it is an Armstrong
    number, False otherwise.
    An Armstrong number is a number that is equal to the sum of its digits
    raised to the power of the number of digits.

    For example:
    is_armstrong(1) returns True
    is_