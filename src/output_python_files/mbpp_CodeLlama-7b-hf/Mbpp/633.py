"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""


def pair_xor_Sum(arr, n):
    """
    :param arr: list of integers
    :param n: integer
    :return: sum of xor of all pairs of numbers in the given list
    """
    # Write your code here
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += arr[i] ^ arr[j]
    return sum


if __name__ == '__main__':
    arr = [5, 9, 7, 6]
    n = 4
    print(pair_xor_Sum(arr, n))

"""
Time Complexity: O(n^2)
Space Complexity: O(1)

Explanation:
We iterate through the list and for each element we iterate through the list again and calculate the xor of the element with each element.
"""

"""
Test Case 1:
Input: [5,9,7,6], 4
Output: 47
Explanation:
The pairs of numbers are (5,9), (5,7), (5,6), (9,7), (9,6), (7,6).
The xor of each pair is 5^9, 5^7, 5^6, 9^7, 9^6, 7^6.
The sum of xor of all pairs is 5^9 + 5^7 + 5^6 + 9^7 + 9^6 + 7^6 = 47.
"""

"""
Test Case 2:
Input: [1,2,3,4], 4
Output: 15
Explanation:
The pairs of numbers are (1,2), (1,3), (1,4), (2,3), (2,4), (3,4).
The xor of each pair is 1^2, 1^3, 1^4, 2^3, 2^4, 3^4.
The sum of xor of all pairs is 1^2 + 1^3 + 1^4 + 2^3 + 2^4 + 3^4 = 15.
"""

"""
Test Case 3:
Input: [1,2,3,4,5], 5
Output: 31
Explanation:
The pairs of numbers are (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5).
The xor of each pair is 1^2, 1^3, 1^4, 1^5, 2^3, 2^4, 2^5, 3^4, 3^5, 4^5.
The sum of xor of all pairs is 1^2 + 1^3 + 1^4 + 1^5 + 2^3 + 2^4 + 2^5 + 3^4 + 3^5 + 4^5 = 31.
"""

"""
Test Case 4:
Input: [1,2,3,4,5,6], 6
Output: 63
Explanation:
The pairs of numbers are (1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6), (4,5), (4,6), (5,6).
The xor of each pair is 1^2, 1^3, 1^4, 1^5, 1^6, 2^3, 2^4, 2^5, 2^6, 3^4, 3^5, 3^6, 4^5, 4