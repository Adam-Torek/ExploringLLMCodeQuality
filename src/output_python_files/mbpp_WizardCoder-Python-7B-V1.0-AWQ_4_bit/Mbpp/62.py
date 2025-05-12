"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest_num(lst):
    return min(lst)

print(smallest_num([10, 20, 1, 45, 99])) # Output: 1
print(smallest_num([-5, 0, 100, 5, -10])) # Output: -10
print(smallest_num([100, 50, 30, 20, 40])) # Output: 100
print(smallest_num([-10, -5, -8, -100, -20])) # Output: -20
print(smallest_num([1, 2, 3, 4, 5])) # Output: 1
print(smallest_num([-1, -2, -3, -4, -5])) # Output: -5
print(smallest_num([0, 0, 0, 0, 0])) # Output: 0
print(smallest_num([1, 1, 1, 1, 1])) # Output: 1
print(smallest_num([-1, -1, -1, -1, -1])) # Output: -1
print(smallest_num([1.1, 2.2, 3.3, 4.4, 5.5])) # Output: 1.1
print(smallest_num([-1.1, -2.2, -3.3, -4.4, -5.5])) # Output: -5.5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 1
print(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # Output: -10
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5])) # Output: 1
print(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1.1, -2.2, -3.3, -4.4, -5.5])) # Output: -10
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5, -1, -2, -3, -4, -5])) # Output: -5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5, -1, -2, -3, -4, -5, -1.1, -2.2, -3.3, -4.4, -5.5])) # Output: -5.5
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5, -1, -2, -3, -4, -5, -1.1, -2.2, -3.3, -4.4, -5.5, 0, 0, 0, 0, 0])) # Output: 0
print(smallest_num([1, 2, 3, 4, 5