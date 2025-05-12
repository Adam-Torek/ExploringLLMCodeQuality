def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

def is_sorted(l: list):
    """Return True if a list is sorted in ascending order
    >>> is_sorted([5, 3, 5, 2, 3, 3, 9, 0, 123])
    False
    >>> is_sorted([0, 2, 3, 5, 9, 123])
    True
    """

def is_anagram(s1: str, s2: str):
    """Return True if s1 and s2 are anagrams
    >>> is_anagram('abc', 'cba')
    True
    >>> is_anagram('abc', 'cb')
    False
    """

def is_palindrome(s: str):
    """Return True if s is a palindrome
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('race')
    False
    """

def is_pangram(s: str):
    """Return True if s is a pangram
    >>> is_pangram('the quick brown fox jumps over the lazy dog')
    True
    >>> is_pangram('the quick brown fox jumps over the lazy cat')
    False
    """

def is_isogram(s: str):
    """Return True if s is an isogram
    >>> is_isogram('abc')
    True
    >>> is_isogram('abbc')
    False
    """

def is_prime(n: int):
    """Return True if n is prime
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    False
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    >>> is_prime(21)
    False
    >>> is_prime(22)
    False
    >>> is_prime(23)
    True
    >>> is_prime(24)
    False
    >>> is_prime(25)
    False
    >>> is_prime(26)
    False
    >>> is_prime(27)
    False
    >>> is_prime(28)
    False
    >>> is_prime(29)
    True
    >>> is_prime(30)
    False
    >>> is_prime(31)
    True
    >>> is_prime(32)
    False
    >>> is_prime(33)
    False
    >>> is_prime(34)
    False
    >>> is_prime(35)
    False
    >>> is_prime(36)
    False
    >>> is_prime(37)
    True
    >>> is_prime(38)
    False
    >>> is_prime(39)
    False
    >>> is_prime(40)
    False
    >>> is_prime(41)
    True
    >>> is_prime(42)
    False
    >>> is_prime(43)
    True
    >>> is_prime(44)
    False
    >>> is_prime(45)
    False
    >>> is_prime(46)
    False
    >>> is_prime(47)
    True
    >>> is_prime(48)
    False
    >>> is_prime(49)
    False
    >>> is_prime(50)
    False
    >>> is_prime(51)
    False
    >>> is_prime(52)
    False
    >>> is_prime(53)
    True
    >>> is_prime(54)
    False
    >>> is_prime(55)
    False
    >>> is_prime(56)
    False
    >>> is_prime(57)
    False
    >>> is