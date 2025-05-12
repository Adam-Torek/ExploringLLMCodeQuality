"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""

def max_sub_array_sum_repeated(arr, k, n):
    if k == 1:
        return max(arr)
    if k > n:
        return max(arr) * n
    max_sum = 0
    for i in range(n):
        sum = 0
        for j in range(i, i + k):
            sum += arr[j % n]
        max_sum = max(max_sum, sum)
    return max_sum

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
<file_sep>/leetcode/1001-1100/1013. Partition Array Into Three Parts With Equal Sum.py
"""
1013. Partition Array Into Three Parts With Equal Sum
Easy

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] +... + A[i] == A[i+1] + A[i+2] +... + A[j-1] == A[j] + A[j-1] +... + A[A.length - 1])

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3!= 0:
            return False
        target = total // 3
        count = 0
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            if sum == target:
                count += 1
                sum = 0
        return count == 3
<file_sep>/leetcode/1001-1100/1005. Maximize Sum Of Array After K Negations.py
"""
1005. Maximize Sum Of Array After K Negations
Easy

Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""

class Solution:
    def largestSumAfterKNegations