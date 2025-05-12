def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    return is_prime(len(string))

# Testing
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
print(prime_length('12345'))
print(prime_length('123456'))
print(prime_length('1234567'))
print(prime_length('12345678'))
print(prime_length('123456789'))
print(prime_length('1234567891'))
print(prime_length('12345678910'))
print(prime_length('12345678911'))
print(prime_length('12345678912'))
print(prime_length('12345678913'))
print(prime_length('12345678914'))
print(prime_length('12345678915'))
print(prime_length('12345678916'))
print(prime_length('12345678917'))
print(prime_length('12345678918'))
print(prime_length('12345678919'))
print(prime_length('12345678920'))
print(prime_length('12345678921'))
print(prime_length('12345678922'))
print(prime_length('12345678923'))
print(prime_length('12345678924'))
print(prime_length('12345678925'))
print(prime_length('12345678926'))
print(prime_length('12345678927'))
print(prime_length('12345678928'))
print(prime_length('12345678929'))
print(prime_length('12345678930'))
print(prime_length('12345678931'))
print(prime_length('12345678932'))
print(prime_length('12345678933'))
print(prime_length('12345678934'))
print(prime_length('12345678935'))
print(prime_length('12345