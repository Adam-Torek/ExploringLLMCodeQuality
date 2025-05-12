"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""

def get_max_sum(n):
    if n <= 1:
        return n
    max_sum = 0
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                for l in range(1, n):
                    if i + j + k + l == n:
                        max_sum = max(max_sum, get_max_sum(i) + get_max_sum(j) + get_max_sum(k) + get_max_sum(l))
    return max_sum

def get_max_sum_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            for k in range(1, i):
                for l in range(1, i):
                    if j + k + l == i:
                        dp[i] = max(dp[i], dp[j] + dp[k] + dp[l])
    return dp[n]

print(get_max_sum(60))
print(get_max_sum_dp(60))
<file_sep>/leetcode/1000+/1000+/1000_1099/1089_duplicate_zeros.py
"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
        return arr
<file_sep>/leetcode/1000+/1000+/1000_1099/1085_sum_of_digits_in_the_minimum_number.py
"""
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
Return 0 if S is odd, otherwise return 1.

Example 1:
Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation:
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.

Example 2:
Input: [99,77,33,66,55]
Output: 1
Explanation:
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.

Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
"""

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 1 if sum(map(int, str(min(A)))) % 2 else 0
<file_sep>/leetcode/1000+/1000+/1000_1099/1086_high_five.sql
# Write your MySQL query statement below
select
    id,
    (select
        round(avg(score),