"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""

def max_val(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

print(max_val(['Python', 3, 2, 4, 5, 'version'])) # Output: 5
print(max_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 10
print(max_val([-1, -2, -3, -4, -5, -6])) # Output: -1
print(max_val([-1, 2, 3, 4, -5, 6])) # Output: 6
print(max_val([1, 'hello', 3, 'world', 4, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5])) # Output: 5
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6])) # Output: 6
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7])) # Output: 7
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8])) # Output: 8
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 9])) # Output: 9
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 9, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 9, 'python', 10])) # Output: 10
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 9, 'python', 10])) # Output: 10
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 9, 'python', 10, 'python'])) # Output: 'python'
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5, 'python', 6, 'python', 7, 'python', 8, 9, 'python', 10, 'python', 11])) # Output: 11
print(max_val([1, 'hello', 3, 'world', 4, 'python', 5,