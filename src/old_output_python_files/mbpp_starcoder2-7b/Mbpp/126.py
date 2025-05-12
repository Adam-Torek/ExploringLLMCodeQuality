"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_common_divisors(a, b):
    """
    >>> sum_common_divisors(10, 15)
    6
    """
    return sum(common_divisors(a, b))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
<file_sep>/python/0001-0500/0101-0150/0140-0149/0148-maximum-gap.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by HazzaCheng on 2020-07-14
# https://leetcode.com/problems/maximum-gap/

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

        如果数组元素个数小于 2，则返回 0。

        示例 1:

        输入: [3,6,9,1]
        输出: 3
        解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
        示例 2:

        输入: [10]
        输出: 0
        解释: 数组元素个数小于 2，因此返回 0。
        说明:

        你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
        请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/maximum-gap
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap


if __name__ == '__main__':
    print(Solution().maximumGap([3, 6, 9, 1]))  # 3
    print(Solution().maximumGap([10]))  # 0
<file_sep>/python/0001-0500/0401-0450/0415-add-strings.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by HazzaCheng on 2020-07-20
# https://leetcode.com/problems/add-strings/

import unittest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

        Note:

        The length of both num1 and num2 is < 5100.
        Both num1 and num2 contains only digits 0-9.
        Both num1 and num2 does not contain any leading zero.
        You must not use any built-in BigInteger library or convert the inputs to integer directly.

        Example 1:

        Input: num1 = "11", num2 = "123"
        Output: "134"
        Example 2:

        Input: num1 = "456", num2 = "77"
        Output: "533"
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = num1.zfill(len(num2))
        res = []
        carry = 0
        for i in range(len(num1) - 1, -1, -1):
            tmp = int(num1[i]) + int(num2[i]) + carry
            res.append(str(tmp % 10))
            carry = tmp // 10
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1