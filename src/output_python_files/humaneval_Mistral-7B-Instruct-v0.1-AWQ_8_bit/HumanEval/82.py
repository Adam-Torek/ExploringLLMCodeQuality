def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check if the string is empty
    if len(string) == 0:
        return False
    # check if the string is a prime number
    for i in range(2, len(string)):
        if string[0:i] == string[i:]:
            return False
    return True

# test the function
print(prime_length('Hello')) # True
print(prime_length('abcdcba')) # True
print(prime_length('kittens')) # True
print(prime_length('orange')) # False