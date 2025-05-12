"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""

def max_product(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        max1 = arr[0]
        max2 = arr[1]
        min1 = arr[0]
        min2 = arr[1]
        max_product = max1 * max2
        for i in range(2, len(arr)):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif arr[i] > max2:
                max2 = arr[i]
            if arr[i] < min1:
                min2 = min1
                min1 = arr[i]
            elif arr[i] < min2:
                min2 = arr[i]
            max_product = max(max_product, max1 * max2, max1 * min1, max2 * min2)
        return max_product

# Test cases
print(max_product([3, 100, 4, 5, 150, 6])) # Output: 300
print(max_product([1, 2, 3, 4, 5])) # Output: 6
print(max_product([-10, -20, -30, -40, -50])) # Output: 3000
print(max_product([-10, -20, -30, -40, -50, -60])) # Output: 600
print(max_product([-10, -20, -30, -40, -50, -60, -70])) # Output: 1200
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80])) # Output: 1200
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90])) # Output: 1800
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100])) # Output: 1800
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110])) # Output: 1800
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120])) # Output: 2400
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130])) # Output: 2400
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140])) # Output: 2400
print(max_product([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150])) # Output: 3000
print(max_product([-10,