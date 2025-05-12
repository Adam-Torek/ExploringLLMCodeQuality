"""
Write a python function to find the maximum difference between any two elements in a given array.
assert max_Abs_Diff((2,1,5,3)) == 4
"""

def max_Abs_Diff(arr):
    return max(abs(max(arr) - min(arr)))

print(max_Abs_Diff((2,1,5,3)) == 4) # True
print(max_Abs_Diff((1, 5, 10, 100, 20, 30, 40)) == 90) # True
print(max_Abs_Diff((-10, -5, -3, -6) == 15) # True
print(max_Abs_Diff((1, 2, 3, 4, 5) == 4) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6) == 5) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7) == 6) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8) == 7) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9) == 8) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 9) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == 10) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == 11) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) == 12) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) == 13) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) == 14) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16) == 15) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17) == 16) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18) == 17) # True
print(max_Abs_Diff((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19) == 18) # True
print(max_Abs_Diff((1, 2, 3, 4, 5,