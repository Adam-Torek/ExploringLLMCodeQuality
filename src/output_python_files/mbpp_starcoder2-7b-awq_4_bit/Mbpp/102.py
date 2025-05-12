"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(s):
    return ''.join([i.capitalize() if i!='_' else '' for i in s.split('_')])

print(snake_to_camel('python_program'))
/leetcode/1001-1100/1001-1010/1009.py
"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:
Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""

class Solution:
    def smallest_difference(self, A, K):
        A.sort()
        return min([A[i+K]-A[i] for i in range(len(A)-K)])

A = [1,3,6]
K = 3
print(Solution().smallest_difference(A, K))
/leetcode/1001-1100/1001-1010/1006.py
"""
Given two integers A and B, return any string S such that:
S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.

Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.

Example 2:
Input: A = 4, B = 1
Output: "aabaa"

Note:
0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""

class Solution:
    def __init__(self):
        self.A = 0
        self.B = 0

    def smallest_string(self, A, B):
        self.A = A
        self.B = B
        return self.smallest_string_helper(A, B)

    def smallest_string_helper(self, A, B):
        if A == 0:
            return 'b'*B
        if B == 0:
            return 'a'*A
        if A == B:
            return 'ab'*A
        if A > B:
            return 'a' + self.smallest_string_helper(A-1, B)
        if A < B:
            return 'b' + self.smallest_string_helper(A, B-1)

A = 4
B = 1
print(Solution().smallest_string(A, B))
/leetcode/1001-1100/1001-1010/1003.py
"""
Given a string S, we are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: "abcd"
Output: "dcbabcd"

Note:
The length of S will be in the range [0, 1,000].
S will only contain lowercase letters.
"""

class Solution:
    def shortest_palindrome(self, s):
        if s == s