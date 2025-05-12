def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def is_prime(num):
    """Given a number return True if it is a prime number and False if it is not.

    Note: A prime number is only divisible by 1 and itself.

    Example:
        is_prime(1) ==> False
        is_prime(2) ==> True
        is_prime(-1) ==> False
        is_prime(7) ==> True
    """

def is_palindrome(word):
    """Given a string, return True if the string is a palindrome. If not, return False.

    Note: A palindrome is a word that is spelled the same forward and backward.

    Example:
        is_palindrome("racecar") ==> True
        is_palindrome("walter") ==> False
    """

def is_pangram(sentence):
    """Given a string, return True if it is a pangram. If not, return False.

    Note: Pangrams are words or sentences containing every letter of the alphabet at least once.

    Example:
        is_pangram("The quick brown fox jumps over the lazy dog") ==> True
        is_pangram("You shall not pass!") ==> False (not "You shall not PASS!")
    """

def is_anagram(word1, word2):
    """Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (just rearranged).

    Note: Anagrams are case insensitive

    Example:
        is_anagram("", "I am a weakish speller") ==> True
        is_anagram("Twas brillig and the slithy toves", "Just gimme a brick") ==> False
    """

def is_isogram(word):
    """Given a string, return True if the string is an isogram. If not, return False.

    Note: An isogram is a word that has no duplicate letters.

    Example:
        is_isogram("lumberjack") ==> True
        is_isogram("background") ==> False
        is_isogram("abcdefg") ==> True
    """

def is_armstrong(num):
    """Given a number determine if it is an Armstrong number.

    Note: An n-digit number that is the sum of the nth powers of its digits is called an Armstrong number.

    Example:
        is_armstrong(153) ==> True
        is_armstrong(123) ==> False
    """

def is_strong(num):
    """Given a number determine if it is a strong number.

    Note: A number is strong if the sum of the factorial of each digit is equal to number itself.

    Example:
        is_strong(145) ==> False (not 1! + 4! + 5! = 145)
        is_strong(1331) ==> True (1! + 3! + 3! + 1! = 1331)
    """

def is_deficient(num):
    """Given a number determine if it is a deficient number.

    Note: A number is deficient if the sum of its factors is less than the number itself.

    Example:
        is_deficient(12) ==> False (6 + 3 + 2 = 11 < 12)
        is_deficient(18) ==> True (6 +