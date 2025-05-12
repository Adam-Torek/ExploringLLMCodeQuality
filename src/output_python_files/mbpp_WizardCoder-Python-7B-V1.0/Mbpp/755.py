"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(lst):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest

print(second_smallest([1, 2, -8, -2, 0, -2])) # -2
print(second_smallest([5, 5, 5, 5, 5])) # None
print(second_smallest([-1, -2, -3, -4])) # -3
print(second_smallest([0, 0, 0, 0])) # None
print(second_smallest([1, 2, 3, 4, 5])) # 2
print(second_smallest([-1, -2, -3, -4, -5])) # -3
print(second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 3
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # 5
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # 5
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1])) # -1
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2])) # -1
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3])) # -2
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4])) # -2
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5])) # -3
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6])) # -3
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7])) # -3
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8])) # -4
print(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9])) # -4
print(second_smallest([10, 9, 8,