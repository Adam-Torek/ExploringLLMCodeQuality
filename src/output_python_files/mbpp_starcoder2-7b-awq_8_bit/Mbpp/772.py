"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""

def remove_length(string, k):
    words = string.split()
    result = []
    for word in words:
        if len(word)!= k:
            result.append(word)
    return''.join(result)

print(remove_length('The person is most value tet', 3))
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

class Solution(object):
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

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return int(''.join(['0' if i == '1' else '1' for i in bin(N)[2:]]), 2)

print(Solution().bitwiseComplement(5))
/python/leetcode/easy/1013_partition_array_into_three_parts_with_equal_sum.py
"""
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] +... + A[i] == A[i+1] + A[i+2] +... + A[j-1] == A[j] + A[j-1] +... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1