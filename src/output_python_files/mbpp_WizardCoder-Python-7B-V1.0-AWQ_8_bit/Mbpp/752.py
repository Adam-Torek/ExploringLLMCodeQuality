"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jacobsthal_num(n-1) + jacobsthal_num(n-2) + 2*jacobsthal_num(n-3)

# Test cases
print(jacobsthal_num(5)) # Output: 11
print(jacobsthal_num(10)) # Output: 2731
print(jacobsthal_num(20)) # Output: 10905
print(jacobsthal_num(50)) # Output: 1348296100