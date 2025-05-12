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
    Write a function that takes an integer n and returns True 
    if this integer is a prime number.
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
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_palindrome(s):
    '''
    Write a function that takes a string s and returns True 
    if this string is a palindrome.
    Note: you may assume the input is always valid.
    Examples:
    is_palindrome('abba') ==> True
    is_palindrome('abcd') ==> False
    is_palindrome('a') ==> True
    is_palindrome('') ==> True
    is_palindrome('aA') ==> True
    is_palindrome('abAba') ==> True
    '''
    return s == s[::-1]


def is_perfect_square(n):
    '''
    Write a function that takes an integer n and returns True 
    if this integer is a perfect square.
    Note: you may assume the input is always valid.
    Examples:
    is_perfect_square(1) ==> False
    is_perfect_square(2) ==> True
    is_perfect_square(3) ==> False
    is_perfect_square(4) ==> True
    is_perfect_square(5) ==> False
    is_perfect_square(6) ==> True
    is_perfect_square(7) ==> False
    is_perfect_square(8) ==> True
    is_perfect_square(9) ==> False
    is_perfect_square(10) ==> True
    is_per