def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    return a**(1/3) == int(a**(1/3))


def is_prime(n):
    '''
    Write a function that takes an integer n and returns True if n is a prime number.
    Note: you may assume the input is always valid.
    Examples:
    is_prime(1) ==> False
    is_prime(2) ==> True
    is_prime(3) ==> True
    is_prime(4) ==> False
    is_prime(5) ==> True
    is_prime(6) ==> False
    is_prime(7) ==> True
    is_prime(8) ==> False
    is_prime(9) ==> False
    is_prime(10) ==> False
    is_prime(11) ==> True
    is_prime(12) ==> False
    is_prime(13) ==> True
    is_prime(14) ==> False
    is_prime(15) ==> False
    is_prime(16) ==> False
    is_prime(17) ==> True
    is_prime(18) ==> False
    is_prime(19) ==> True
    is_prime(20) ==> False
    '''
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_palindrome(s):
    '''
    Write a function that takes a string s and returns True if s is a palindrome.
    Note: you may assume the input is always valid.
    Examples:
    is_palindrome('a') ==> True
    is_palindrome('aa') ==> True
    is_palindrome('ab') ==> False
    is_palindrome('aba') ==> True
    is_palindrome('abc') ==> False
    is_palindrome('abcba') ==> True
    is_palindrome('abcbaa') ==> False
    '''
    return s == s[::-1]


def is_permutation(s1, s2):
    '''
    Write a function that takes two strings s1 and s2 and returns True if s1 is a permutation of s2.
    Note: you may assume the input is always valid.
    Examples:
    is_permutation('a', 'a') ==> True
    is_permutation('a', 'b') ==> False
    is_permutation('ab', 'ba') ==> True
    is_permutation('ab', 'baa') ==> False
    is_permutation('ab', 'b') ==> False
    is_permutation('ab',