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
    # 1. Check if the input is empty string or not
    if num == "":
        return 0
    # 2. Convert the input to a list of integers
    num_list = [int(i, 16) for i in num]
    # 3. Count the number of primes
    count = 0
    for i in num_list:
        if i in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count


if __name__ == "__main__":
    print(hex_key("AB"))
    print(hex_key("1077E"))
    print(hex_key("ABED1A33"))
    print(hex_key("123456789ABCDEF0"))
    print(hex_key("2020"))
    print(hex_key(""))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0"))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0"))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0"))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0"))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0"))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0"))
    print(hex_key("123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF012345678