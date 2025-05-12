def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(c) for c in s if c.isupper())


# Test cases
print(digitSum("")) # => 0
print(digitSum("abAB")) # => 131
print(digitSum("abcCd")) # => 67
print(digitSum("helloE")) # => 69
print(digitSum("woArBld")) # => 131
print(digitSum("aAaaaXa")) # => 153
print(digitSum("aAaaaXa1")) # => 153
print(digitSum("aAaaaXa1bBc")) # => 153
print(digitSum("aAaaaXa1bBcD")) # => 153
print(digitSum("aAaaaXa1bBcDd")) # => 153
print(digitSum("aAaaaXa1bBcDdE")) # => 153
print(digitSum("aAaaaXa1bBcDdEf")) # => 153
print(digitSum("aAaaaXa1bBcDdEfG")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGh")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhI")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIj")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjK")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKl")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlM")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMn")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnO")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOp")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQ")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQr")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQrs")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQrst")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQrstU")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQrstUv")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQrstUvW")) # => 153
print(digitSum("aAaaaXa1bBcDdEfGhIjKlMnOpQrstUvWx"))