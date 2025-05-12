"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""

def merge_sorted_list(list1, list2, list3):
    """
    :param list1:
    :param list2:
    :param list3:
    :return:
    """
    list1.extend(list2)
    list1.extend(list3)
    list1.sort()
    return list1

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))/python/leetcode/easy/1002_find_common_characters.py
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

def commonChars(A):
    """
    :param A:
    :return:
    """
    result = []
    for i in range(len(A[0])):
        count = 0
        for j in range(len(A)):
            if A[j][i] in result:
                count += 1
            else:
                result.append(A[j][i])
        if count == len(A):
            result.append(A[0][i])
    return result

print(commonChars(["bella","label","roller"]))
print(commonChars(["cool","lock","cook"]))/python/leetcode/easy/1009_complement_of_base_10_integer.py
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

def bitwiseComplement(N):
    """
    :param N:
    :return: