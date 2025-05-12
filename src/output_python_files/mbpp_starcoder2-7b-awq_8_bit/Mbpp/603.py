"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_lucid(n):
    """
    :param n: int
    :return: list
    """
    return [i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0]

if __name__ == '__main__':
    print(get_lucid(10))
/leetcode/easy/1002_find_common_characters.py
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

def common_chars(A):
    """
    :param A: list
    :return: list
    """
    if not A:
        return []
    if len(A) == 1:
        return list(A[0])
    res = []
    for i in range(len(A[0])):
        char = A[0][i]
        for j in range(1, len(A)):
            if char not in A[j]:
                break
            if char in A[j]:
                if A[j].count(char) == 1:
                    res.append(char)
                else:
                    res.extend([char] * A[j].count(char))
    return res

if __name__ == '__main__':
    print(common_chars(["bella","label","roller"]))
    print(common_chars(["cool","lock","cook"]))
/leetcode/easy/1003_check_if_word_is_valid_after_substitutions.py
"""
Given a string s, a substitution rule rule is given by a string two strings: start and end.

It can be applied on any substring of s that matches start once. It creates a new string by replacing any and all occurrences of start with end.

Return true if it is possible to apply the rule to all the substrings of s and make s equal to result.

Example 1:

Input: s = "abcd", rule = "bcdf"
Output: true
Explanation:
Since a rule matches substrings "bcd" and "cdf", a substitution can be made on those substrings with itself.
Also, there will not be any further substitutions, since s is already equal to result.
Example 2:

Input: s = "abcd", rule = "acd"
Output: false
Explanation:
It is impossible to get s = result after any substitution.
Example 3:

Input: s = "aababab", rule = "ab"
Output: true
Explanation:
The first "ab" in s can be replaced by "c" to get s = "cacabb", which is equal to result.
The second "ab" in the original s can be replaced by "c" to get s = "aabcac", which is equal to result.
Note:

0 <= len(s) <= 1000
0 <= len(rule) = len(start) = len(end) <= 100
s, start and end consist of lower case English letters.
"""

def check_valid_substitution(s, rule):
    """
    :param s: str
    :param rule: str
    :return: bool
    """
    if not s or not rule:
        return False
    if len(s)!= len(rule):
        return False
    if len(s) == 1:
        return s == rule
    if len(s) == 2:
        return s == rule
    if len(s) == 3:
        return s == rule
    if len(s) == 4:
        return s == rule
    if len(s) == 5:
        return s == rule
    if len(s) == 6:
        return s == rule
    if len(s)