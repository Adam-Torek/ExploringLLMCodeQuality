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
print(digitSum("")) # Output: 0
print(digitSum("abAB")) # Output: 131
print(digitSum("abcCd")) # Output: 67
print(digitSum("helloE")) # Output: 69
print(digitSum("woArBld")) # Output: 131
print(digitSum("aAaaaXa")) # Output: 153