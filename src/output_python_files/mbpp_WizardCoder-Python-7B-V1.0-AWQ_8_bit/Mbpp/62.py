"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest_num(lst):
    return min(lst)

print(smallest_num([10, 20, 1, 45, 99])) # Output: 1
print(smallest_num([-5, 0, 10, 20, -10])) # Output: -10
print(smallest_num([-10, -5, -20, -40])) # Output: -40
print(smallest_num([10.5, 20.25, 1.25, 45.75])) # Output: 1.25
print(smallest_num([1, 2, 3, 4, 5])) # Output: 1
print(smallest_num([-1, -2, -3, -4, -5])) # Output: -5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 1
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])) # Output: 0
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1])) # Output: -1
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5])) # Output: -5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0])) # Output: -5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0, 100, 200, 300])) # Output: -5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0, 100, 200, 300, 10000])) # Output: -5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0, 100, 200, 300, 10000, 0.5])) # Output: 0.5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0, 100, 200, 300, 10000, 0.5, 100000])) # Output: 0.5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0, 100, 200, 300, 10000, 0.5, 100000, 1000000])) # Output: 0.5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, 0, 100, 200,