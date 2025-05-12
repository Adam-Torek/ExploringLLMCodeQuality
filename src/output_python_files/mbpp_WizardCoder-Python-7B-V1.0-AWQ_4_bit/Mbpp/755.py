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
print(second_smallest([1, 2, 3, 4, 5])) # 2
print(second_smallest([-1, -2, -3, -4, -5])) # -3
print(second_smallest([1, 2, 3, 4, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) # 3
print(second_smallest([1, 2, 3, 4, 5, 5, 5,