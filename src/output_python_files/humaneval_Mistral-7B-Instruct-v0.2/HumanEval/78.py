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
    hex_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    prime_digits = 0
    for digit in num:
        decimal_digit = hex_to_decimal[digit]
        if decimal_digit <= 9:
            if is_prime(decimal_digit):
                prime_digits += 1
        elif decimal_digit >= 10 and decimal_digit <= 15:
            if is_prime(decimal_digit - 10):
                prime_digits += 1
    return prime_digits

def is_prime(num):
    """You have to write a function that checks if a given number is prime.
    A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
    Examples:
    For num = 2 the output should be True.
    For num = 3 the output should be True.
    For num = 5 the output should be True.
    For num = 7 the output should be True.
    For num = 10 the output should be False.
    For num = 15 the output should be False.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Testing
print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))</s>