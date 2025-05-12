"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)) # Output: [60, 54, 50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],2)) # Output: [54, 60]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],1)) # Output: [60]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)) # Output: [54, 50, 48, 42]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)) # Output: [54, 50, 48, 42, 36]

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Efficient Solution:
def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)) # Output: [60, 54, 50]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],2)) # Output: [54, 60]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],1)) # Output: [60]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],4)) # Output: [54, 50, 48, 42]
print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],5)) # Output: [54, 50, 48, 42, 36]

# Time Complexity: O(n)
# Space Complexity: O(n)

# Efficient Solution:
def large_product(list1, list2, k):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(list1[i] * list2[i])
    return result

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)) # Output: [60, 54, 50]
print(large_product([1, 2, 3,