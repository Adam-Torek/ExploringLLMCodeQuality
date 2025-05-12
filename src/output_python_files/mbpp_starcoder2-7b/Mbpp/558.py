"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(num1, num2):
    """
    >>> digit_distance_nums(1,2)
    1
    """
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) > len(num2):
        num2 = '0'*(len(num1)-len(num2)) + num2
    elif len(num1) < len(num2):
        num1 = '0'*(len(num2)-len(num1)) + num1
    return sum([int(num1[i]) - int(num2[i]) for i in range(len(num1))])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
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
A[i][j] is a lowercase letter
"""

def commonChars(A):
    """
    >>> commonChars(["bella","label","roller"])
    ['e', 'l', 'l']
    >>> commonChars(["cool","lock","cook"])
    ['c', 'o']
    """
    result = []
    for i in range(len(A[0])):
        char = A[0][i]
        for j in range(1, len(A)):
            if char not in A[j]:
                break
            if A[j].count(char) < A[0].count(char):
                char = A[j][A[j].index(char)]
        result.append(char)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
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
"""

def bitwiseComplement(N):
    """
    >>> bitwiseComplement(5)
    2
    >>> bitwiseComplement(7)
    0
    >>> bitwiseComplement(10)
    5
    """
    return int(''.join(['1' if i == '0' else '0' for i in bin(N)[2:]]), 2)

if __name__ == '__main__':
    import doctest
    doctest.test