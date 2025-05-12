"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""

def get_lucid(n):
    """
    :param n: int
    :return: list
    """
    lucid = []
    for i in range(1, n+1):
        if i == 1:
            lucid.append(i)
        else:
            if i % 2 == 0:
                lucid.append(i)
            else:
                if i % 3 == 0:
                    lucid.append(i)
                else:
                    if i % 5 == 0:
                        lucid.append(i)
    return lucid

print(get_lucid(10))
/leetcode/1001-1100/1009.py
"""
1009. Complement of Base 10 Integer

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
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        else:
            return int(''.join(['1' if i == '0' else '0' for i in bin(N)[2:]]), 2)


if __name__ == '__main__':
    s = Solution()
    print(s.bitwiseComplement(5))
    print(s.bitwiseComplement(7))
    print(s.bitwiseComplement(10))
/leetcode/1001-1100/1003.py
"""
1003. Check If Word Is Valid After Substitutions

Given a string S, a k duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make k duplicate removals on S, until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.



Example 1:

Input: "abcd"
Output: "abcd"
Explanation: If we choose to remove duplicate characters in order, we will get "abcd".
Example 2:

Input: "abccba"
Output: "a"
Explanation: If we choose to remove duplicate characters in order, we will get "a".
Note that "abccba" also applies, since removing "bb" would not make the string equal to "a".
Example 3:

Input: "aabcabcab"
Output: ""
Explanation: If we choose to remove duplicate characters in order, we will get "".
Example 4:

Input: "aaabaaab"
Output: "aaabaaab"
Example 5:

Input: "aaababab"
Output: "ab"


Note:

1 <= S.length <= 10^5
S consists only of lowercase letters.
"""


class Solution:
    def isValid(self, S: str) -> bool:
        """
        :type