"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""

def find_remainder(arr, n):
    result = 1
    for i in arr:
        result = (result * i) % n
    return result

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11)) # Output: 9

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another solution:

def find_remainder(arr, n):
    return reduce(lambda x, y: (x*y) % n, arr)

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11)) # Output: 9

# Time Complexity: O(n)
# Space Complexity: O(1)

# Using reduce() function from the functools module in Python to multiply all the elements of the array and then taking the modulo with n.