def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """

def is_prime(num):
    """You have been tasked to write a function that receives a number 
    and returns True if it is a prime number, and False otherwise.
    Examples:
    For num = 1 the output should be False.
    For num = 2 the output should be True.
    For num = 3 the output should be True.
    For num = 4 the output should be False.
    For num = 5 the output should be True.
    For num = 6 the output should be False.
    For num = 7 the output should be True.
    For num = 8 the output should be False.
    For num = 9 the output should be False.
    For num = 10 the output should be False.
    For num = 11 the output should be True.
    For num = 12 the output should be False.
    For num = 13 the output should be True.
    For num = 14 the output should be False.
    For num = 15 the output should be False.
    For num = 16 the output should be False.
    For num = 17 the output should be True.
    For num = 18 the output should be False.
    For num = 19 the output should be True.
    For num = 20 the output should be False.
    For num = 21 the output should be False.
    For num = 22 the output should be False.
    For num = 23 the output should be True.
    For num = 24 the output should be False.
    For num = 25 the output should be False.
    For num = 26 the output should be False.
    For num = 27 the output should be False.
    For num = 28 the output should be False.
    For num = 29 the output should be True.
    For num = 30 the output should be False.
    For num = 31 the output should be True.
    For num = 32 the output should be False.
    For num = 33 the output should be False.
    For num = 34 the output should be False.
    For num = 35 the output should be False.
    For num = 36 the output should be False.
    For num = 37 the output should be True.
    For num = 38 the output should be False.
    For num = 39 the output should be False.
    For num = 40 the output should be False.
    For num = 41 the output should be True.
    For num = 42 the output should be False.
    For num = 43 the output should be True.
    For num = 44 the output should be False.
    For num = 45 the output should be False.
    For num = 46 the output should be False.
    For num = 47 the output should be True.
    For num = 48 the output should be False.
    For num = 49 the output should be False.
    For num = 50 the output should be False.
    For num = 51 the output should be False.
    For num = 52 the output should be False.
    For