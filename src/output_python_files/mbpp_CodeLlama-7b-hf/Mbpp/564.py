"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count


if __name__ == '__main__':
    arr = [1,2,1]
    n = 3
    print(count_Pairs(arr,n))

"""
Time Complexity: O(n^2)
Space Complexity: O(1)

Explanation:
We iterate through the list and for each element we iterate through the rest of the list and check if the element is unequal to the current element.

Sample Input:
arr = [1,2,1]
n = 3

Sample Output:
2

Explanation:
We have 2 possible pairs:
1,2
2,1
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count
"""

"""
def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[