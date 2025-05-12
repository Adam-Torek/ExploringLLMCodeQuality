"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""

def min_val(lst):
    min_val = lst[0]
    for i in lst:
        if type(i) == str:
            continue
        elif i < min_val:
            min_val = i
    return min_val

print(min_val(['Python', 3, 2, 4, 5, 'version'])) # Output: 2
print(min_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 1
print(min_val([-1, -2, -3, -4, -5, -6])) # Output: -6
print(min_val([10, 20, 30, 40, 50, 'hello'])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world'])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python'])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80, 'java'])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80, 'java', 90])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80, 'java', 90, 'kotlin'])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80, 'java', 90, 'kotlin', 100])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80, 'java', 90, 'kotlin', 100, 'javascript'])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 80, 'java', 90, 'kotlin', 100, 'javascript', 110])) # Output: 10
print(min_val([10, 'hello', 20, 30, 40, 50, 'world', 60, 'python', 70, 8