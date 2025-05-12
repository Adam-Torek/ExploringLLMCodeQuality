"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1,list2,n):
    list1.sort()
    list2.sort()
    list1.reverse()
    list2.reverse()
    return [list1[i]*list2[i] for i in range(n)]

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))
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
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        if len(A) == 1:
            return list(A[0])
        res = []
        for i in range(len(A[0])):
            c = A[0][i]
            for j in range(1, len(A)):
                if c not in A[j]:
                    break
                if A[j].count(c) < A[0].count(c):
                    c = A[j][A[0].index(c)]
            res.append(c)
        return res
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
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join('0' if i == '1' else '1' for i in bin(N)[2:]), 2)
/python/leetcode/easy/1018_Binary_Prefix_Divisible_By_5.py
"""
Given an array A of strings, return true if there is a string in the array that starts with exactly A[i] + A[i+1] +... + A[i+k] where:

k >= 0
i, k < A.length
If there is such