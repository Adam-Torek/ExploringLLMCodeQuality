"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""

def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("python program"))
/python/leetcode/easy/1002_find_common_characters.py
"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i] consists of lowercase letters
"""

def common_characters(A):
    result = []
    for i in range(len(A[0])):
        char = A[0][i]
        for j in range(1, len(A)):
            if char not in A[j]:
                break
            if char in A[j]:
                if A[j].count(char) == 1:
                    result.append(char)
                else:
                    char = A[j][A[j].index(char)+1]
    return result

print(common_characters(["bella","label","roller"]))
print(common_characters(["cool","lock","cook"]))
/python/leetcode/easy/1003_check_if_word_is_valid_after_substitutions.py
"""
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform it via following operations:

Insert a character in t at any position.
Remove any character in t with a length of 1.
Replace any character in t with another character.
Return true if s is a valid string or false otherwise.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"a" -> "a"
"abc" -> "a" + "bc" -> "abcbc"
"abcbc" -> "ab" + "cbc" -> "abcbc"
There are 4 steps to transform s to an empty string.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"abcabcabc" -> "abc" + "abc" + "abc" = "abcabcabc"
"abcabc" -> "abc" + "abc" = "abcabc"
"abcabc" -> "ab" + "cabc" = "abcabc"
There are 3 steps to transform s to an empty string.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get an empty string using the operations.
Example 4:

Input: s = "cababc"
Output: false
Explanation: It is impossible to get an empty string using the operations.

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
"""

def check_valid_string(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "c":
            stack.append(i)
        elif s[i] == "b":
            if len(stack) > 0:
                stack.pop()
        elif s[i] == "a":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return True

print(check_valid_string("aabcbc"))
print(check_valid_string("abcabcababcc"))
print(check_valid_string("abccba"))
print(check_valid_string("cababc"))
/python/leetcode/easy/1001_grid_illumination.py
"""
On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-