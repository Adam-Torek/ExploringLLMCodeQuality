"""
Write a function to calculate the sum of perrin numbers.
assert cal_sum(9) == 49
"""

def cal_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return cal_sum(n-1) + cal_sum(n-2) + cal_sum(n-3)

print(cal_sum(9))
/python/leetcode/1001-1100/1005.py
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3] and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
/python/leetcode/1001-1100/1007.py
"""
Given an array A of non-negative integers, return the largest number that can be formed by concatenating the elements of A.

The length of A will be between 1 and 16.
The elements of A will be between 0 and 9.
The number of elements in A will be between 1 and 16.

Example 1:

Input: [10,2]
Output: 210

Example 2:

Input: [3,30,34,5,9]
Output: 9534330

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    def largestNumber(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A = [str(x) for x in A]
        A.sort(key=lambda x: x * 10 ** len(x), reverse=True)
        return str(int(''.join(A)))
/python/leetcode/1001-1100/1009.py
"""
Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.

The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the sum of the two previous numbers. The first six numbers of the Fibonacci sequence are then:

1, 1, 2, 3, 5 and 8.

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than 10 are 1, 1, 3, and 5.

sumFibs(1) should return 1
sumFibs(1000) should return 1785
"""

def sumFibs(num):
    """
    :type num: int
    :rtype: int
    """
    a, b = 1, 1
    sum = 0
    while b <= num:
        if b % 2!= 0:
            sum += b
        a, b = b, a + b
    return sum

print(sumFibs(1000))
/python/leetcode/1001-1100/1006.py
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:

Input