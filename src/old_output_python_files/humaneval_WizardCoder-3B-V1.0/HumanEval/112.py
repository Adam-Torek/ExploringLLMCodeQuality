def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

# Solution
def reverse_delete(s, c):
    # Create a set of characters to delete
    delete_set = set(c)

    # Iterate through the string and delete characters that match the delete set
    result = ""
    for char in s:
        if char not in delete_set:
            result += char

    # Check if the result is a palindrome
    is_palindrome = result == result[::-1]

    return (result, is_palindrome)

# Test cases
print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))  # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)<|endoftext|>