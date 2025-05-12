"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(s):
    return tuple(map(int, s[1:-1].split(', ')))

print(tuple_str_int("(7, 8, 9)"))
/python/leetcode/1001-1100/1007. Minimum Domino Rotations For Equal Row.py
"""
1007. Minimum Domino Rotations For Equal Row
Medium

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if A[0] == B[0]:
            return min(self.count(A, B, A[0]), self.count(A, B, B[0]))
        else:
            return min(self.count(A, B, A[0]), self.count(A, B, B[0]), self.count(A, B, A[0], B[0]))
        
    def count(self, A, B, x, y=None):
        if y is None:
            y = x
        count = 0
        for i in range(len(A)):
            if A[i]!= x and B[i]!= x and A[i]!= y and B[i]!= y:
                return -1
            if A[i]!= x and B[i]!= y:
                count += 1
        return count
/python/leetcode/1001-1100/1003. Check If Word Is Valid After Substitutions.py
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

Input: s = "cab