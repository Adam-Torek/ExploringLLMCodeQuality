"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(s):
    return ''.join([x.capitalize() if x!='_' else '' for x in s.split('_')])

print(snake_to_camel('python_program'))
/python/leetcode/1001-1100/1009.complement-of-base-10-integer.py
"""
1009. Complement of Base 10 Integer
Easy

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

0 <= N < 10^9
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join(['1' if x=='0' else '0' for x in bin(N)[2:]]), 2)
/python/leetcode/1001-1100/1003.check-if-word-is-valid-after-substitutions.py
"""
1003. Check If Word Is Valid After Substitutions
Medium

Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t.  More formally, t becomes tleft + "abc" + tright, where t == tleft + tright.  Note that tleft and tright may be empty.

Return true if s is a valid string, otherwise, return false.

 

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
Example 4:

Input: s = "cababc"
Output: false
Explanation: It is impossible to get "cababc" using the operation.
 

Constraints:

1 <= s.length <= 2 * 104
s consists of lowercase English letters.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        while 'abc' in s:
            s = s.replace('abc', '')
        return s==''
/python/leetcode/1001-1100/1007.minimum-domino-rotations-for-equal-row.py
"""
1007. Minimum Domino Rotations For Equal Row
Medium

In a