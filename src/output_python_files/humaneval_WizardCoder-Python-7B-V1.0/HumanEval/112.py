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
    s = ''.join([i for i in s if i not in c])
    return (s, s == s[::-1])


# Test cases
print(reverse_delete("abcde", "ae")) # should return ('bcd', False)
print(reverse_delete("abcdef", "b")) # should return ('acdef', False)
print(reverse_delete("abcdedcba", "ab")) # should return ('cdedc', True)