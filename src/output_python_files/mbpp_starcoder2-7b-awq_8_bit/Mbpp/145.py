"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""

def max_Abs_Diff(arr):
    max_diff = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) > max_diff:
                max_diff = abs(arr[i] - arr[j])
    return max_diff

print(max_Abs_Diff((2,1,5,3)))
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

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return []
        if len(A) == 1:
            return list(A[0])
        common_chars = list(A[0])
        for i in range(1, len(A)):
            common_chars = self.find_common_chars(common_chars, A[i])
        return common_chars

    def find_common_chars(self, common_chars, A):
        common_chars_copy = common_chars[:]
        for char in common_chars_copy:
            if char not in A:
                common_chars.remove(char)
        for char in A:
            if char not in common_chars:
                common_chars.append(char)
        return common_chars

s = Solution()
print(s.commonChars(["bella","label","roller"]))
print(s.commonChars(["cool","lock","cook"]))
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

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        binary_str = bin(N)[2:]
        complement = ""
        for char in binary_str:
            if char == "0":
                complement += "1"
            else:
                complement += "0"
        return int(complement, 2)

s