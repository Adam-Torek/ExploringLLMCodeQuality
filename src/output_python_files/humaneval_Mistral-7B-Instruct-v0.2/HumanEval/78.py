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
    decimal_num = ''
    prime_count = 0
    for digit in num:
        decimal_num += str(hex_to_decimal[digit])
        if is_prime(int(decimal_num[-1])):
            prime_count += 1
        decimal_num = decimal_num[:-1]
    return prime_count

def is_prime(num):
    """You have to write a function that checks if a given number is prime.
    A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
    Examples:
    For num = 2 the output should be True.
    For num = 3 the output should be True.
    For num = 4 the output should be False.
    For num = 5 the output should be True.
    For num = 17 the output should be True.
    """
    if num < 2:
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
print(hex_key("2020"))