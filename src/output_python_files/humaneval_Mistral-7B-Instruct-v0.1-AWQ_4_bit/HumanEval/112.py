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
    s = list(s)
    c = list(c)
    s = [c.count(x) > 0 for x in s]
    s = [x for x in s if x != 0]
    s = ''.join(s)
    return s,s == s[::-1]


s = "abcde"
c = "ae"
print(reverse_delete(s,c))

s = "abcdef"
c = "b"
print(reverse_delete(s,c))

s = "abcdedcba"
c = "ab"
print(reverse_delete(s,c))