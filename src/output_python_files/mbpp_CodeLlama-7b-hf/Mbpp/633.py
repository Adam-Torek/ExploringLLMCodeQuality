"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""


def pair_xor_Sum(arr, n):
    """
    :param arr: list of integers
    :param n: number of elements in the list
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
We iterate through the list and for each element we iterate through the list again and calculate the xor of the two elements.
"""

"""
Test Case:
Input: [5,9,7,6], 4
Output: 47

Explanation:
The pairs of numbers are (5,9), (5,7), (5,6), (9,7), (9,6), (7,6).
The xor of these pairs is 5^9 = 4, 5^7 = 6, 5^6 = 7, 9^7 = 16, 9^6 = 15, 7^6 = 13.
The sum of these xor is 4+6+7+16+15+13 = 47.
"""

"""
Test Case:
Input: [1,2,3,4], 4
Output: 20

Explanation:
The pairs of numbers are (1,2), (1,3), (1,4), (2,3), (2,4), (3,4).
The xor of these pairs is 1^2 = 3, 1^3 = 2, 1^4 = 5, 2^3 = 6, 2^4 = 8, 3^4 = 7.
The sum of these xor is 3+2+5+6+8+7 = 20.
"""

"""
Test Case:
Input: [1,2,3,4,5], 5
Output: 30

Explanation:
The pairs of numbers are (1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5).
The xor of these pairs is 1^2 = 3, 1^3 = 2, 1^4 = 5, 1^5 = 4, 2^3 = 6, 2^4 = 8, 2^5 = 7, 3^4 = 7, 3^5 = 6, 4^5 = 1.
The sum of these xor is 3+2+5+4+6+7+7+6+1 = 30.
"""

"""
Test Case:
Input: [1,2,3,4,5,6], 6
Output: 42

Explanation:
The pairs of numbers are (1,2), (1,3), (1,4), (1,5), (1,6), (2,3), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6), (4,5), (4,6), (5,6).
The xor of these pairs is 1^2 = 3, 1^3 = 2, 1^4 = 5, 1^5 = 4, 1^6 = 3, 2^3 = 6, 2^4 = 8, 2^5 = 7, 2^6 = 6, 3^4 = 7, 3^5 = 6, 3^6 = 5, 4