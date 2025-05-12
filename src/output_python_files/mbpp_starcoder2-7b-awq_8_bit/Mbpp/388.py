"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    return 2 ** (n.bit_length() - 1)

print(highest_Power_of_2(10))
/python/leetcode/easy/1002_Find_Common_Characters.py
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

class Solution:
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
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
                if A[j].count(char) < A[0].count(char):
                    char = A[j][A[0].index(char)]
            res.append(char)
        return res

A = ["bella","label","roller"]
print(Solution().commonChars(A))
/python/leetcode/easy/1009_Complement_of_Base_10_Integer.py
"""
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

The given number is guaranteed to fit within the range from 0 to 10^9.
"""

class Solution:
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        res = 0
        while N > 0:
            res = res * 2 + 1
            N = N // 2
        return res

print(Solution().bitwiseComplement(5))
/python/leetcode/easy/1007_Minimum_Domino_Rotations_For_Equal_Row.py
"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of