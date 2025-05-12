"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""

def find_length(binary_string):
    """
    :param binary_string: str
    :return: int
    """
    # TODO: Write your code here
    pass


if __name__ == '__main__':
    print(find_length("11000010001"))
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

from collections import Counter


def find_common_characters(strings):
    """
    :param strings: List[str]
    :return: List[str]
    """
    # TODO: Write your code here
    pass


if __name__ == '__main__':
    print(find_common_characters(["bella", "label", "roller"]))
    print(find_common_characters(["cool", "lock", "cook"]))
/leetcode/easy/1003_check_if_word_is_valid_after_substitutions.py
"""
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform every next character of the given string s into t by performing any of the following operations:

Insert a character into t at any position.
Delete the last character of t.
Replace the last character of t with any character of s.
Return true if s is a valid string, otherwise return false.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"a" -> ""    remove
"ab" -> "c"  insert
"abc" -> "bc" delete
"abcb" -> "bcb" insert
"abcbc" -> "bcb" delete

Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"a" -> ""    remove
"ab" -> "c"  insert
"abc" -> "bc" delete
"abcb" -> "bcb" insert
"abcbc" -> "bcb" delete
"abcab" -> "bcb" insert
"abcabc" -> "bcb" delete
"abcabcb" -> "bcb" insert
"abcabcbc" -> "bcb" delete

Example 3:

Input: s = "abccba"
Output: false

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
"""


def check_valid_string(s):
    """
    :param s: str
    :return: bool
    """
    # TODO: Write your code here
    pass


if __name__ == '__main__':
    print(check_valid_string("aabcbc"))
    print(check_valid_string("abcabcababcc"))
    print(check_valid_string("abccba"))
/leetcode/easy/1001_find_common_characters.py
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
1 <= A[