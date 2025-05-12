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
    return s, s == s[::-1]


s = "abcde"
c = "ae"
print(def_delete(s,c))

s = "abcdef"
c = "b"
print(def_delete(s,c))

s = "abcdedcba"
c = "ab"
print(def_delete(s,c))


# Output:
# ('bcd', False)
# ('acdef', False)
# ('cdedc', True)