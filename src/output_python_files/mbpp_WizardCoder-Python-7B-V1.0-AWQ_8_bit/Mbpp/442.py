"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""

def positive_count(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count/len(arr)

print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])) # 0.54
print(positive_count([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 1.0
print(positive_count([-1, -2, -3, -4, -5, -6, -7, -8, -9])) # 0.0
print(positive_count([0, 0, 0, 0, 0, 0, 0, 0])) # 0.0
print(positive_count([1, 1, 1, 1, 1, 1, 1, 1])) # 1.0
print(positive_count([-1, -1, -1, -1, -1, -1, -1, -1])) # 0.0
print(positive_count([])) # 0.0

# Test cases
# Test case 1: [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
# Expected output: 0.54

# Test case 2: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output: 1.0

# Test case 3: [-1, -2, -3, -4, -5, -6, -7, -8, -9]
# Expected output: 0.0

# Test case 4: [0, 0, 0, 0, 0, 0, 0, 0]
# Expected output: 0.0

# Test case 5: [1, 1, 1, 1, 1, 1, 1, 1]
# Expected output: 1.0

# Test case 6: [-1, -1, -1, -1, -1, -1, -1, -1]
# Expected output: 0.0

# Test case 7: []
# Expected output: 0.0

# Test case 8: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: 1.0

# Test case 9: [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# Expected output: 0.0

# Test case 10: [0, 0, 0, 0, 0, 0, 0, 0, 1]
# Expected output: 0.1

# Test case 11: [-1, -2, -3, -4, -5, -6, -7, -8, -9, 1]
# Expected output: 0.1

# Test case 12: [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# Expected output: 0.0

# Test case 13: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: 1.0

# Test case 14: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Expected output: 1.0

# Test case 1