"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square_test(matrix):
    """
    :param matrix:
    :return:
    """
    if len(matrix)!= 4:
        return False
    if len(matrix[0])!= 4:
        return False
    for i in range(4):
        if sum(matrix[i])!= 34:
            return False
    for i in range(4):
        if sum([matrix[j][i] for j in range(4)])!= 34:
            return False
    if matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3]!= 34:
        return False
    if matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0]!= 34:
        return False
    return True


if __name__ == '__main__':
    print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
/leetcode/1001-1100/1001-1010/1005.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:    1005
Description : 
Author :      wellqin
date:         2020/5/10
-------------------------------------------------
Change Activity:
2020/5/10:
-------------------------------------------------
"""
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


def sort_array_by_parity(A):
    """
    :param A:
    :return:
    """
    return sorted(A, key=lambda x: x % 2)


if __name__ == '__main__':
    print(sort_array_by_parity([3, 1, 2, 4]))
/leetcode/1001-1100/1001-1010/1006.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:    1006
Description : 
Author :      wellqin
date:         2020/5/10
-------------------------------------------------
Change Activity:
2020/5/10:
-------------------------------------------------
"""
"""
The Tower of Hanoi is a famous game in which a player must move a stack of disks from one rod to another. There are three rods and n disks on the first rod. The objective of the game is to move the entire stack to the last rod, obeying the following rules:

Only one disk can be moved at a time.
A disk can be moved only if it is the uppermost disk on a rod.
No disk can be placed on top of a smaller disk.
Given n, the number of disks, return the minimum number of moves required to move the entire stack to the last rod, or -1 if this is impossible.

 

Example 1:

Input: n = 4
Output: 6
Explanation: In the first move, we will have discs 1, 2, 3, 4 as [1,2,3,4], in the second move, we will have discs 1, 3, 4, 2 as [1,3,4,2], and finally in the third move, we will have discs 2