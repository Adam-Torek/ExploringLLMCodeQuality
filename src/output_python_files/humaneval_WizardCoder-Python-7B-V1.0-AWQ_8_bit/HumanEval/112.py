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



# Test cases
print(defer_delete("abcde", "ae"))  # should return ('bcd', False)
print(defer_delete("abcdef", "b"))  # should return ('acdef', False)
print(defer_delete("abcdedcba", "ab"))  # should return ('cdedc', True)
print(defer_delete("abccba", "ab"))  # should return ('c', True)
print(defer_delete("abba", "ab"))  # should return ('', True)
print(defer_delete("racecar", "r"))  # should return ('cecar', True)
print(defer_delete("hello", "lo"))  # should return ('he', False)
print(defer_delete("abcd", "z"))  # should return ('abcd', False)
print(defer_delete("", "a"))  # should return ('', True)
print(defer_delete("a", "a"))  # should return ('', True)
print(defer_delete("aa", "a"))  # should return ('', True)
print(defer_delete("abba", "a"))  # should return ('bb', True)
print(defer_delete("abba", "b"))  # should return ('a', False)
print(defer_delete("abba", "c"))  # should return ('abba', False)
print(defer_delete("abba", "abba"))  # should return ('', True)
print(defer_delete("abba", "abcd"))  # should return ('abba', False)
print(defer_delete("abba", "abba"))  # should return ('', True)
print(defer_delete("abba", "a"))  # should return ('b', False)
print(defer_delete("abba", "b"))  # should return ('a', False)
print(defer_delete("abba", "c"))  # should return ('abba', False)
print(defer_delete("abba", "abba"))  # should return ('', True)