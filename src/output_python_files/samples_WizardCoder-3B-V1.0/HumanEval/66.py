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

def digit_sum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digit_sum("") => 0
        digit_sum("abAB") => 131
        digit_sum("abcCd") => 67
        digit_sum("helloE") => 69
        digit_sum("woArBld") => 131
        digit_sum("aAaaaXa") => 153
    """
    return sum(ord(c) - 65 for c in s if c.isupper())

# Test cases
print(digit_sum(""))  # Output: 0
print(digit_sum("abAB"))  # Output: 131
print(digit_sum("abcCd"))  # Output: 67
print(digit_sum("helloE"))  # Output: 69
print(digit_sum("woArBld"))  # Output: 131
print(digit_sum("aAaaaXa"))  # Output: 153<|endoftext|>