def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

def is_palindrome(string):
    """Write a function that takes a string and returns True if the string
    is a palindrome or False otherwise
    Examples
    is_palindrome('racecar') == True
    is_palindrome('hello') == False
    is_palindrome('kayak') == True
    """

def is_anagram(string1, string2):
    """Write a function that takes two strings and returns True if the strings
    are anagrams or False otherwise
    Examples
    is_anagram('hello', 'olleh') == True
    is_anagram('hello', 'olleh') == True
    is_anagram('hello', 'olleh') == True
    """

def is_pangram(string):
    """Write a function that takes a string and returns True if the string
    is a pangram or False otherwise
    Examples
    is_pangram('The quick brown fox jumps over the lazy dog') == True
    is_pangram('The quick brown fox jumps over the lazy dog') == True
    is_pangram('The quick brown fox jumps over the lazy dog') == True
    """

def is_isogram(string):
    """Write a function that takes a string and returns True if the string
    is an isogram or False otherwise
    Examples
    is_isogram('hello') == False
    is_isogram('hello') == False
    is_isogram('hello') == False
    """

def is_palindrome_isogram(string):
    """Write a function that takes a string and returns True if the string
    is a palindrome and an isogram or False otherwise
    Examples
    is_palindrome_isogram('hello') == False
    is_palindrome_isogram('hello') == False
    is_palindrome_isogram('hello') == False
    """

def is_palindrome_isogram_anagram(string1, string2):
    """Write a function that takes two strings and returns True if the strings
    are anagrams and palindromes or False otherwise
    Examples
    is_palindrome_isogram_anagram('hello', 'olleh') == False
    is_palindrome_isogram_anagram('hello', 'olleh') == False
    is_palindrome_isogram_anagram('hello', 'olleh') == False
    """

def is_palindrome_isogram_anagram_pangram(string1, string2):
    """Write a function that takes two strings and returns True if the strings
    are anagrams, palindromes, and pangrams or False otherwise
    Examples
    is_palindrome_isogram_anagram_pangram('hello', 'olleh') == False
    is_palindrome_isogram_anagram_pangram('hello', 'olleh') == False
    is_palindrome_isogram_anagram_pangram('hello', 'olleh') == False
    """

def is_palindrome_isogram_anagram_pangram_prime(string1, string2):
    """Write a function that takes two strings and returns True if the strings
    are anagrams, palindromes, pangrams, and prime numbers or False otherwise
    Examples
    is_palindrome_isogram_anagram_pangram_prime('hello', 'olleh') == False
    is_palindrome_isogram_anagram_pangram_prime('hello',