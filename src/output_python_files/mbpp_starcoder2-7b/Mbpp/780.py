"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            result.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return result

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
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
A[i][j] is a lowercase letter
"""

class Solution:
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []
        for i in range(len(A[0])):
            char = A[0][i]
            count = 0
            for j in range(len(A)):
                if char in A[j]:
                    count += 1
            if count == len(A):
                result.append(char)
        return result

print(Solution().commonChars(["bella","label","roller"]))
/python/leetcode/easy/1009_complement_of_base_10_integer.py
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
        binary = bin(N)[2:]
        result = ""
        for i in range(len(binary)):
            if binary[i] == "0":
                result += "1"
            else:
                result += "0"
        return int(result, 2)

print(Solution().bitwiseComplement(5))
/python/leetcode/easy/1013_partition_