"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""

def find_Index(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return -1
    arr = [0]
    for i in range(1, n+1):
        arr.append(i)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if arr[i] + arr[j] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[0]


if __name__ == '__main__':
    print(find_Index(2))