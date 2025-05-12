"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""

def max_difference(list_of_tuples):
    """
    :param list_of_tuples: list of tuples
    :return: max difference between available pairs in the given tuple list
    """
    max_diff = 0
    for i in range(len(list_of_tuples)):
        for j in range(i + 1, len(list_of_tuples)):
            if abs(list_of_tuples[i][0] - list_of_tuples[j][0]) > max_diff:
                max_diff = abs(list_of_tuples[i][0] - list_of_tuples[j][0])
    return max_diff


if __name__ == '__main__':
    print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))
<file_sep>/python/leetcode/easy/1002_find_common_characters.py
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
A[i][j] is a lowercase letter
"""

from collections import Counter


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
        common_chars = Counter(A[0])
        for i in range(1, len(A)):
            common_chars = common_chars & Counter(A[i])
        return list(common_chars.elements())


if __name__ == '__main__':
    print(Solution().commonChars(["bella", "label", "roller"]))
    print(Solution().commonChars(["cool", "lock", "cook"]))
<file_sep>/python/leetcode/easy/1009_complement_of_base_10_integer.py
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

0 <= N < 10^9
"""


class Solution:
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        binary_str = bin(N)[2:]
        complement = ''
        for bit in binary_str:
            if bit == '1':
                complement += '0'
            else:
                complement