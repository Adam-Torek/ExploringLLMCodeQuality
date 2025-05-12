"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""

def smallest_num(lst):
    return min(lst)

print(smallest_num([10, 20, 1, 45, 99])) # Output: 1
print(smallest_num([-5, 0, 10, -10, 5])) # Output: -10
print(smallest_num([100, 200, 300, 400])) # Output: 100
print(smallest_num([-100, -200, -300, -400])) # Output: -400
print(smallest_num([1, 2, 3, 4, 5])) # Output: 1
print(smallest_num([-1, -2, -3, -4, -5])) # Output: -5
print(smallest_num([10.5, 20.2, 30.1, 40.6])) # Output: 10.5
print(smallest_num([-10.5, -20.2, -30.1, -40.6])) # Output: -40.6
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 1
print(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # Output: -10
print(smallest_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])) # Output: 1.1
print(smallest_num([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -1.1, -2.2, -3.3, -4.4, -5.5, -6.6, -7.7, -8.8, -9.9])) # Output: -9.9
print(smallest_num([])) # Output: None
print(smallest_num([1])) # Output: 1
print(smallest_num([-1])) # Output: -1
print(smallest_num([0])) # Output: 0
print(smallest_num([0, 0])) # Output: 0
print(smallest_num([1, 0])) # Output: 0
print(smallest_num([-1, 0])) # Output: -1
print(smallest_num([0, -1])) # Output: -1
print(smallest_num([0, 0, 0])) # Output: 0
print(smallest_num([1, 2, 3, "a", 4, 5])) # Output: None
print(smallest_num([1, 2, 3, "a", 4, 5, 6])) # Output: None
print(smallest_num([1, 2, 3, "a", 4, 5, 6, 7])) # Output: None
print(smallest_num([1, 2, 3, "a", 4, 5, 6, 7, 8])) # Output: None
print(smallest_num([1, 2, 3, "a", 4, 5, 6, 7, 8, 9])) # Output: None
print(smallest_num([1, 2, 3, "a", 4, 5, 6, 7, 8, 9, 10])) # Output: None
print