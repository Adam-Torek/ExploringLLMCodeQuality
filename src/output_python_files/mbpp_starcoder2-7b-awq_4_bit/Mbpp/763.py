"""
Write a python function to find the minimum difference between any two elements in a given array. https://www.geeksforgeeks.org/find-minimum-difference-pair/
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""

def find_min_diff(arr, k):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff

assert find_min_diff((1,5,3,19,18,25),6) == 1
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

def find_common_characters(A):
    if not A:
        return []
    if len(A) == 1:
        return list(A[0])
    common_chars = list(A[0])
    for i in range(1, len(A)):
        common_chars = [c for c in common_chars if c in A[i]]
    return common_chars

assert find_common_characters(["bella","label","roller"]) == ['e', 'l', 'l']
assert find_common_characters(["cool","lock","cook"]) == ['c', 'o']
/python/leetcode/easy/1003_check_if_word_is_valid_after_substitutions.py
"""
Given a string s, return true if the s can be made only of letters 'a' and 'b' after performing the following operation:

Pick a non-empty substring of s and replace it with either 'a' or 'b'.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
s = "aabcbc" after the first replacement operation, we get the string "aabcbc".
Since there are no instances of substring "ab", we return true.
Example 2:

Input: s = "aabccabba"
Output: false
Explanation:
s = "aabccabba" after the first replacement operation, we get the string "abccabba".
Now, there is one instance of substring "ab", but it is not a substring of the whole string.

Constraints:

1 <= s.length <= 1000
s[i] is either 'a' or 'b'.
"""

def check_if_valid_substitution(s):
    if not s:
        return True
    stack = []
    for c in s:
        if c == 'a':
            stack.append(c)
        elif c == 'b':
            if not stack or stack.pop()!= 'a':
                return False
    return not stack

assert check_if_valid_substitution("aabcbc") == True
assert check_if_valid_substitution("aabccabba") == False
/python/leetcode/easy/1001_grid_illumination.py
"""
On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th lamp, the i-th lamp lights those squares [x, y] where 0 <= x < N and 0 <= y < N and x