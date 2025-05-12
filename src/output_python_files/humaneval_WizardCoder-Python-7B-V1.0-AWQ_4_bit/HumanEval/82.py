def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    n = len(string)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



# Test cases
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False
print(prime_length('123'))  # False
print(prime_length(''))  # False
print(prime_length('a'))  # False
print(prime_length('1'))  # False
print(prime_length('2'))  # True
print(prime_length('11'))  # True
print(prime_length('233'))  # True
print(prime_length('1234'))  # False
print(prime_length('12345'))  # False
print(prime_length('123456'))  # False
print(prime_length('1234567'))  # False
print(prime_length('12345678'))  # False
print(prime_length('123456789'))  # False
print(prime_length('1234567890'))  # False
print(prime_length('12345678901'))  # False
print(prime_length('123456789012'))  # False
print(prime_length('1234567890123'))  # False
print(prime_length('12345678901234'))  # False
print(prime_length('123456789012345'))  # False
print(prime_length('1234567890123456'))  # False
print(prime_length('12345678901234567'))  # False
print(prime_length('123456789012345678'))  # False
print(prime_length('1234567890123456789'))  # False
print(prime_length('12345678901234567890'))  # False
print(prime_length('123456789012345678901'))  # False
print(prime_length('1234567890123456789012'))  # False
print(prime_length('12345678901234567890123'))  # False
print(prime_length('12345678901234567890