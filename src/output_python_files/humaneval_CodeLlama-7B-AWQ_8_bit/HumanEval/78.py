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
    # your code here
    count = 0
    for i in num:
        if i.isdigit():
            if i == '2' or i == '3' or i == '5' or i == '7':
                count += 1
        else:
            if i == 'B' or i == 'D':
                count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(hex_key("AB"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")